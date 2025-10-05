# SMSApp/views.py
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import StudentManagement
from .serializers import StudentManagementSerializer

# List all students
class StudentListAPI(GenericAPIView):
    serializer_class = StudentManagementSerializer
    queryset = StudentManagement.objects.all()

    def get(self, request):
        try:
            students = self.get_queryset()
            serializer = self.get_serializer(students, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Create a new student
class StudentCreateAPI(GenericAPIView):
    serializer_class = StudentManagementSerializer

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Student added successfully!'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Retrieve a single student
class StudentDetailAPI(GenericAPIView):
    serializer_class = StudentManagementSerializer
    queryset = StudentManagement.objects.all()

    def get(self, request, pk):
        try:
            student = self.get_queryset().get(pk=pk)
            serializer = self.get_serializer(student)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except StudentManagement.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Update a student
class StudentUpdateAPI(GenericAPIView):
    serializer_class = StudentManagementSerializer
    queryset = StudentManagement.objects.all()

    def put(self, request, pk):
        try:
            student = self.get_queryset().get(pk=pk)
            serializer = self.get_serializer(student, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Student updated successfully!'}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except StudentManagement.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Delete a student
class StudentDeleteAPI(GenericAPIView):
    serializer_class = StudentManagementSerializer
    queryset = StudentManagement.objects.all()

    def delete(self, request, pk):
        try:
            student = self.get_queryset().get(pk=pk)
            student.delete()
            return Response({'message': 'Student deleted successfully!'}, status=status.HTTP_200_OK)
        except StudentManagement.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
