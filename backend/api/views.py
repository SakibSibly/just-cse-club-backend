from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import CustomUser, Department, Faculty, Blog, Comment, Event, Notice
from .serializers import CustomUserSerializer
from .serializers import DepartmentSerializer, FacultySerializer, BlogSerializer, CommentSerializer, EventSerializer, NoticeSerializer
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
# from decouple import config
import random

class VerifyEmailView(APIView):
    def post(self, request):
        receiver_email = request.data.get('email')

        if CustomUser.objects.filter(email=receiver_email):
            return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            subject = "JUST CSE Club Account Verification OTP"

            message = "Thank your for registering with JUST CSE Club.\n\nPlease verify your email address.\n\n"
            message += "Your OTP is: " + str(random.randint(100000, 999999))
            message += "\n\nJUST CSE Club"
            message += "\nDepartment of Computer Science and Engineering"
            message += "\nJashore University of Sciene and Technolgy"
            message += "\nJashore, 7408"

            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [receiver_email],
                fail_silently=False
            )
            return Response({'message': 'Mail sent successfully'}, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)

class CustomLoginView(APIView):
    def post(self, request):
        user = get_object_or_404(CustomUser, email=request.data.get('email'))

        if not user.check_password(request.data.get('password')):
            return Response({"details": 'Not Found'}, status=status.HTTP_404_NOT_FOUND)

        token, created = Token.objects.get_or_create(user=user)
        serializer = CustomUserSerializer(instance=user)
        return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_200_OK)
    

class CustomLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out'}, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)
        

class CustomUserCreate(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            user = CustomUser.objects.get(email=request.data.get('email'))
            user.set_password(request.data.get('password'))
            user.save()
            token = Token.objects.create(user=user)
            return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

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
    permission_classes = [IsAuthenticated]

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
    permission_classes = [IsAuthenticated]

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


class BlogListView(APIView):
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        blogs = Blog.objects.all()
        blogs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BlogDetailView(APIView):
    def get_object(self, blog_id):
        try:
            return Blog.objects.get(id=blog_id)
        except Blog.DoesNotExist:
            raise Http404

    def get(self, request, blog_id):
        blog = self.get_object(blog_id)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    def put(self, request, blog_id):
        blog = self.get_object(blog_id)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, blog_id):
        blog = self.get_object(blog_id)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class CommentListView(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        comments = Comment.objects.all()
        comments.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentDetailView(APIView):
    def get_object(self, comment_id):
        try:
            return Comment.objects.get(id=comment_id)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, comment_id):
        comment = self.get_object(comment_id)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, comment_id):
        comment = self.get_object(comment_id)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, comment_id):
        comment = self.get_object(comment_id)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EventListView(APIView):
    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        events = Event.objects.all()
        events.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EventDetailView(APIView):
    def get_object(self, event_id):
        try:
            return Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, event_id):
        event = self.get_object(event_id)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def put(self, request, event_id):
        event = self.get_object(event_id)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, event_id):
        event = self.get_object(event_id)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NoticeListView(APIView):
    def get(self, request):
        notices = Notice.objects.all()
        serializer = NoticeSerializer(notices, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NoticeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        notices = Notice.objects.all()
        notices.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NoticeDetailView(APIView):
    def get_object(self, notice_id):
        try:
            return Notice.objects.get(id=notice_id)
        except Notice.DoesNotExist:
            raise Http404

    def get(self, request, notice_id):
        notice = self.get_object(notice_id)
        serializer = NoticeSerializer(notice)
        return Response(serializer.data)

    def put(self, request, notice_id):
        notice = self.get_object(notice_id)
        serializer = NoticeSerializer(notice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, notice_id):
        notice = self.get_object(notice_id)
        notice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
