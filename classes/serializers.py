from rest_framework import serializers

from .models import Class
from .models import Enrollment

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id','name','schedule','teacher']
        
class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields =['id','student','class_name']