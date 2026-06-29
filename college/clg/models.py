from django.db import models

# Create your models here.
class Department(models.Model):
    hod=models.CharField()
    dept=models.CharField()
    def __str__(self):
        return self.dept
    
class Student(models.Model):
    name=models.CharField()
    email=models.CharField()
    enroll=models.IntegerField()
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)
    def __str__(self):
        return self.name