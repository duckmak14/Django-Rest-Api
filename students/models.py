from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    class_name = models.CharField(max_length=100)
    student_code = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name