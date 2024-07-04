from django.db import models
from students.models import Student
# Create your models here.

class Academic_Record(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    record = models.TextField()
    