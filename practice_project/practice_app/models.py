from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    roll=models.IntegerField()
    city=models.CharField(max_length=30)
    marks=models.IntegerField()
    passdate=models.DateField()
class Teacher(models.Model):
    name=models.CharField(max_length=30)
    empnum=models.IntegerField()
    city=models.CharField(max_length=30)
    salary=models.IntegerField()
    join_date=models.DateField()
    
