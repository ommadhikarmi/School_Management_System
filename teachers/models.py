from django.db import models
from authentication.models import User

# Create your models here.

class Teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    availability = models.TextField()