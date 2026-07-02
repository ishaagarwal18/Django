from rest_framework import serializers
from .models import Student,Faculty

class Facultyserializer(serializers.ModelSerializer):
    class Meta:
        model=Faculty
        fields='__all__'


class Studentserializer(serializers.ModelSerializer):
    std=Facultyserializer(read_only=True,many=True)
    class Meta:
        model=Student
        fields='__all__'