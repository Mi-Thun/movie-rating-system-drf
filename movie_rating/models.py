from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def save(self, *args, **kwargs):
        self.username = self.email  
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.name if self.name else self.email

class Movie(models.Model):
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    rating = models.CharField(max_length=5)
    release_date = models.DateField()

    def __str__(self):
        return self.name

class Rating(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User Name")
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings', verbose_name="Movie Name")
    rating = models.FloatField()
    
    def __str__(self):
        return f'Rating for {self.movie_id} by {self.user_id}'


