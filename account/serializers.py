from rest_framework import serializers
from .tasks import send_activation_code_task
from .models import CustomUser
from django.core.mail import send_mail


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        min_length=4,required=True,
        write_only=True
    )
    password_confirmation = serializers.CharField(
        min_length=4,required=True,
        write_only=True
    )

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email', 'password',
            'password_confirmation',           
        )

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirmation = attrs.pop('password_confirmation')
        if password != password_confirmation:
            msg_ = ("Passwords are not matching...")
            raise serializers.ValidationError(msg_)
        return attrs

    def create(sefl, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        send_activation_code_task.delay(
            user.email,
            user.activation_code
        )
        return user

class ResetPasswordSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ('email',)

    def validate_email(self, email):
        if not CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError("Given user is nonexistent")
        return email

    def send_verification_email(self):
        email = self.validated_data.get('email')
        user = CustomUser.objects.get(email=email)
        user.create_activation_code()
        send_mail(
            'Password reset | パスワードを再設定する',
            f'your reset code is | リセットコードは:  {user.activation_code}',
            'test@gmail.com',
            [user.email]
        )


class CompleteResetPasswordSerializer(serializers.ModelSerializer):
    code = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, min_length=6)
    password_confirmation = serializers.CharField(required=True, min_length=6)

    class Meta:
        model = CustomUser
        fields = (
            'email', 'password', 'code',
            'password_confirmation'           
        )
    def validate(self, data):
        email = data.get('email')
        code = data.get('code')
        password1 = data.get('password')
        password2 = data.get('password_confirmation')

        if not CustomUser.objects.filter(email=email, activation_code=code).exists():
            raise serializers.ValidationError("Wrong email or activation code")

        if password1 != password2:
            raise serializers.ValidationError("Unmatched passwords!")
        return data

    def set_new_password(self):
        email = self.validated_data.get('email')
        password = self.validated_data.get('password')
        user = CustomUser.objects.get(email=email)
        user.set_password(password)
        user.save()