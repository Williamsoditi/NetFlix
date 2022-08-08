from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=100)
    genres=models.CharField(max_length=50)
    poster_path=CloudinaryField('photo')
    overview=models.CharField(max_length=500)
    release_date=models.DateTimeField()


    def save_movie(self):
        self.save()

    def __str__(self):
        return self.title

