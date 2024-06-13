from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .models import Student
from .serializers import StudentSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.views import APIView

# Create your views here

@api_view(http_method_names=["GET", "POST"])
# @permission_classes([AllowAny])
def list_students(request:Request):
    # check post
    students = Student.objects.all()
    serializer = StudentSerializer(instance=students, many=True)
    return Response(data=serializer.data , status=status.HTTP_200_OK)

class StudentView(APIView):
    def get(self,request: Request, id:int):
        student = Student.objects.get(id=id)
        if student: 
            serializer = StudentSerializer(instance=student)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data={"error": "Not found student"}, status=status.HTTP_404_NOT_FOUND) 

    def post(self, request: Request):
        data = request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request: Request,id:int):
        print(id)
        student = get_object_or_404(Student, pk=id)
        data = request.data
        serializer = StudentSerializer(instance=student, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request: Request, id:int):
        print(id)
        student = get_object_or_404(Student, pk=id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)