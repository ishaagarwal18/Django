from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=60)
    director=models.CharField(max_length=60)
    rating=models.IntegerField()
    date=models.DateField()
    def __str__(self):
        return self.name