from django.shortcuts import render
from rest_framework .viewsets import ModelViewSet
from rest_framework .permissions import IsAuthenticated
from rest_framework .filters import SearchFilter,OrderingFilter

from .models import Student

from .serializers import StudentSerializer
# Create your views here.

class StudentView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends =[SearchFilter,OrderingFilter]
    search_fields =['contact_info','user__username']# user__username: This indicates a search within a related model's field. The double underscore (__) syntax is used to traverse relationships between models (commonly seen in Object-Relational Mappers (ORMs) like Django).

