from django.shortcuts import render
from rest_framework .viewsets import ModelViewSet
from .models import Academic_Record
from .serializers import Academic_RecordSerializer
from rest_framework .permissions import IsAuthenticated
# Create your views here.

class Academic_RecordView(ModelViewSet):
    queryset = Academic_Record.objects.all()
    serializer_class = Academic_RecordSerializer
    permission_classes =[IsAuthenticated]
