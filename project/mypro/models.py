from django.db import models

# Create your models here.
class Student(models.Model):
    Name=models.CharField()
    DOB=models.DateField()
    enrollment=models.IntegerField()
    project_title=models.CharField()
    def __str__(self):
        return self.Name
    
class Faculty(models.Model):
    name=models.CharField()
    ptitle=models.ForeignKey(Student,on_delete=models.CASCADE)