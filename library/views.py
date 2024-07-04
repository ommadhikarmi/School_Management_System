from django.shortcuts import render
from rest_framework .viewsets import ModelViewSet
from .models import Book
from .serializers import BookSerializer
from rest_framework .permissions import IsAuthenticated
from .models import BorrowRecord
from .serializers import BorrowRecordSerializer

# Create your views here.

class BookView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes =[IsAuthenticated]

class BorrowRecordView(ModelViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer
    permission_classes =[IsAuthenticated]
