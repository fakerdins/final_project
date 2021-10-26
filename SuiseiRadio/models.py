from django.db import models


class Artist(models.Model):
    artist = models.CharField(
        primary_key=True, max_length=60,
        help_text='instead of using spaces, please user underscores'
    )
    author = models.ForeignKey(
        'account.Customuser',
        on_delete=models.CASCADE,
        related_name='arists',
        help_text='Author means the creator'
    )
    profile_pic = models.ImageField(
        upload_to='pfp_artist',
        verbose_name='Profile image'
    )
    about = models.TextField(blank=True)
    
    def __str__(self):
        return self.artist


class Album(models.Model):
    title = models.CharField(max_length=60)
    about = models.TextField(blank=True)
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE,
        related_name='albums'
    )
    author = models.ForeignKey(
        'account.Customuser',
        on_delete=models.CASCADE,
        related_name='albums',
        help_text='Author means the creator'
    )
    album_cover = models.ImageField(
        upload_to='album_covers',
        verbose_name='Album cover'
    )

    def __str__(self):
        return self.title

class Song(models.Model):
    title = models.CharField(max_length=60)
    audiofile = models.FileField(upload_to='audio_files')
    album = models.ForeignKey(
        Album, on_delete=models.CASCADE,
        related_name='songs'
    )
    author = models.ForeignKey(
        'account.CustomUser',
        on_delete=models.CASCADE,
        related_name='songs'
    )

    def __str__(self):
        return self.title