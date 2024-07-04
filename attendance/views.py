from django.shortcuts import render
from rest_framework .viewsets import ModelViewSet
from .models import Attendance
from .serializers import AttendanceSerializer
from rest_framework .permissions import IsAuthenticated
# Create your views here.

class AttendanceView(ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes =[IsAuthenticated]
