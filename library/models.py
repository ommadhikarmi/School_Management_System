from django.db import models
from authentication.models import User

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100,unique=True)
    author =models.CharField(max_length=100)
    available = models.BooleanField(default=True)

class BorrowRecord(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    borrowed_on = models.DateField()
    return_on = models.DateField(null=True, blank=True)

