from django.db import models
from authentication.models import User
# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    contact_info = models.TextField()
    academics_records = models.TextField()