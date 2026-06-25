from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField()
    roll_no=models.IntegerField()
    enrollment=models.IntegerField()
    title=models.CharField()
    DOB=models.DateField()
    def __str__(self):
        return self.name