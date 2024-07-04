from django.shortcuts import render
from rest_framework .viewsets import ModelViewSet
from.models import Class
from.serializers import ClassSerializer
from rest_framework .permissions import IsAuthenticated
from .models import Enrollment
from .serializers import EnrollmentSerializer

# Create your views here.

class ClassView(ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes =[IsAuthenticated]

class EnrollmentView(ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes =[IsAuthenticated]