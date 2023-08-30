from django.db import models

# Create your models here.

class MovieData(models.Model):

    def __str__(self) -> str:
        return self.name

    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()
    genre = models.CharField(max_length=200, default="drama")
    image = models.ImageField(upload_to='Images/', default='Images/None/Noimg.jpg')

