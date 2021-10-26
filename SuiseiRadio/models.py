from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=60);
    about = models.TextField()
    picture = models.ImageField(upload_to='images', blank=True)
    added_by = models.ForeignKey(
        'account.CustomUser',
        on_delete=models.CASCADE,
        related_name='artists'
    )  

    def __str__(self) -> str:
        return self.name

