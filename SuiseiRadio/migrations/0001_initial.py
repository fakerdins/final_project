# Generated by Django 3.2.7 on 2021-10-27 04:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('about', models.TextField(blank=True)),
                ('album_cover', models.ImageField(upload_to='album_covers', verbose_name='Album cover')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('audiofile', models.FileField(upload_to='audio_files')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='SuiseiRadio.album')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('album', models.ForeignKey(help_text='will write reviews on albums', on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='SuiseiRadio.album')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)], default=None, max_length=1)),
                ('album', models.ForeignKey(help_text='will rate albums', on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='SuiseiRadio.album')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('artist', models.CharField(help_text='instead of using spaces, please use underscores', max_length=60, primary_key=True, serialize=False)),
                ('profile_pic', models.ImageField(upload_to='pfp_artist', verbose_name='Profile image')),
                ('about', models.TextField(blank=True)),
                ('author', models.ForeignKey(help_text='Author means the creator', on_delete=django.db.models.deletion.CASCADE, related_name='arists', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'artists_spotify',
            },
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='SuiseiRadio.artist'),
        ),
        migrations.AddField(
            model_name='album',
            name='author',
            field=models.ForeignKey(help_text='Author means the creator', on_delete=django.db.models.deletion.CASCADE, related_name='albums', to=settings.AUTH_USER_MODEL),
        ),
    ]
