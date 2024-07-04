from rest_framework import serializers
from.models import Academic_Record
class Academic_RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Academic_Record
        fields = '__all__'