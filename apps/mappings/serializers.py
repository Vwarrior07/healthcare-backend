from rest_framework import serializers
from .models import PatientDoctor

class PatientDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDoctor
        fields = '__all__'
        read_only_fields = ['assigned_at']
