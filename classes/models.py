from django.db import models
from teachers.models import Teacher
from students.models import Student
# Create your models here.

class Class(models.Model):
    name = models.CharField(max_length=100)
    schedule = models.TextField()
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)

class Enrollment(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    class_name = models.ForeignKey(Class,on_delete=models.CASCADE)