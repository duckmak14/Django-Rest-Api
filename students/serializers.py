from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
  name = serializers.CharField(max_length=50)
  class Meta:
    model = Student
    fields = (
      'id',
      'name',
      'class_name',
      'student_code',
    )