from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Department, Faculty
from .serializers import DepartmentSerializer, FacultySerializer
from django.http import Http404


class DepartmentListView(APIView):
    def get(self, request):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        departments = Department.objects.all()
        departments.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DepartmentDetailView(APIView):
    def get_object(self, serial_number):
        try:
            return Department.objects.get(serial_number=serial_number)
        except Department.DoesNotExist:
            raise Http404

    def get(self, request, serial_number):
        department = self.get_object(serial_number)
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)

    def put(self, request, department_id):
        department = self.get_object(department_id)
        serializer = DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, department_id):
        department = self.get_object(department_id)
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FacultyListView(APIView):
    def get(self, request):
        faculty = Faculty.objects.all()
        serializer = FacultySerializer(faculty, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FacultySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        faculty = Faculty.objects.all()
        faculty.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class FacultyDetailView(APIView):
    def get_object(self, faculty_id):
        try:
            return Faculty.objects.get(id=faculty_id)
        except Faculty.DoesNotExist:
            raise Http404

    def get(self, request, faculty_id):
        faculty = self.get_object(faculty_id)
        serializer = FacultySerializer(faculty)
        return Response(serializer.data)

    def put(self, request, faculty_id):
        faculty = self.get_object(faculty_id)
        serializer = FacultySerializer(faculty, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, faculty_id):
        faculty = self.get_object(faculty_id)
        faculty.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
