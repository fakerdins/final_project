from django.db import models


class Artist(models.Model):
    artist = models.CharField(
        primary_key=True, max_length=60,
        help_text='instead of using spaces, please use underscores'
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

    class Meta:
        db_table = 'suisei_artists'
    
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

    class Meta:
        db_table = 'suisei_albums'

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

    class Meta:
        db_table = 'suisei_songs'


class Review(models.Model):
    author = models.ForeignKey(
        'account.CustomUser',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name='reviews',
        help_text='will write reviews on albums'        
    )
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.album} | {self.author}'

    class Meta:
        db_table = 'suisei_reviews'

class Like(models.Model):
    class Meta:
        db_table = 'suisei_likes'
    pass

class Rating(models.Model):
    author = models.ForeignKey(
        'account.CustomUser',
        on_delete=models.CASCADE,
        related_name='ratings',
    )
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name='ratings',
        help_text='will rate albums'
    )
    RATE = (
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5)
    )
    rating = models.CharField(max_length=1, choices=RATE, default=None)
    

    def __str__(self):
        return f'{self.author} | {self.album} | {self.rating}' 
    
    class Meta:
        db_table = 'suisei_ratings'
        unique_together = ['album', 'author']