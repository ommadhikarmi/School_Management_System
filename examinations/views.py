from django.shortcuts import render
from rest_framework .viewsets import ModelViewSet
from .models import Examination
from .serializers import ExaminationSerializer
from rest_framework .permissions import IsAuthenticated
from .models import Grade
from .serializers import GradeSerializer

# Create your views here.

class ExaminationView(ModelViewSet):
    queryset = Examination.objects.all()
    serializer_class = ExaminationSerializer
    permission_classes =[IsAuthenticated]

class GradeView(ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes =[IsAuthenticated]