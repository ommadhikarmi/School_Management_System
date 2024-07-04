from django.db import models
from students.models import Student
from teachers. models import Teacher
# Create your models here.

class Examination(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)

class Grade(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    examination = models.ForeignKey(Examination,on_delete=models.CASCADE)
    grade = models.CharField(max_length=10)
