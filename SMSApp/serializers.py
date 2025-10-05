from rest_framework import serializers
from .models import StudentManagement

class StudentManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentManagement
        fields = '__all__'
