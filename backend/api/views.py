from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import CustomUser, OTP, Department, Faculty, Blog, Comment, Event, Notice, Tag, Feedback, Stat, GalleryItem, ResearchCard, AlumniCard, TimeLineItem, FacultyCard, Post
from .serializers import CustomUserSerializer
from .serializers import DepartmentSerializer, FacultySerializer, BlogSerializer, CommentSerializer, EventSerializer, NoticeSerializer, TagSerializer, FeedbackSerializer, StatSerializer, GalleryItemSerializer, ResearchCardSerializer, AlumniCardSerializer, TimeLineItemSerializer, FacultyCardSerializer, PostSerializer
from django.http import Http404
# from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from decouple import config
import random

class VerifyEmailView(APIView):
    def post(self, request):
        receiver_email = request.data.get('email')

        if CustomUser.objects.filter(email=receiver_email):
            return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)
        
        if OTP.objects.filter(email=receiver_email):
            OTP.objects.filter(email=receiver_email).delete()

        try:
            generated_otp = str(random.randint(config('LOWER_BOUNDARY', cast=int), config('UPPER_BOUNDARY', cast=int)))
            otp = OTP(email=receiver_email, otp=generated_otp)
            otp.save()

            subject = "JUST CSE Club Account Verification OTP"

            message = "Thank your for registering with JUST CSE Club.\n\nPlease verify your email address.\n\n"
            message += "Your OTP is: " + generated_otp
            message += "\n\nJUST CSE Club"
            message += "\nDepartment of Computer Science and Engineering"
            message += "\nJashore University of Sciene and Technolgy"
            message += "\nJashore-7408, Bangladesh"

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

class VerifyOTPView(APIView):
    def post(self, request):
        receiver_email = request.data.get('email')
        otp = request.data.get('otp')

        if OTP.objects.filter(email=receiver_email, otp=otp):
            OTP.objects.filter(email=receiver_email).delete()
            return Response({'message': 'OTP verified successfully'}, status=status.HTTP_200_OK)
        
        return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)


class VerifyAdminView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        if request.user.is_staff:
            return Response({'message': 'Admin verified successfully'}, status=status.HTTP_200_OK)
        
        return Response({'error': 'You are not an admin'}, status=status.HTTP_400_BAD_REQUEST)
  

class CustomUserCreate(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)

        if CustomUser.objects.filter(username=request.data.get('username')):
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        
        if CustomUser.objects.filter(email=request.data.get('email')):
            return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            user = CustomUser.objects.get(email=request.data.get('email'))
            user.set_password(request.data.get('password'))
            user.save()
            return Response({'user': serializer.data}, status=status.HTTP_201_CREATED)
        
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
        blogs = Blog.objects.order_by('-created_at')
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    def post(self, request):
        request.data['author'] = request.user.id
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
        events = Event.objects.order_by('-date')
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
        notices = Notice.objects.order_by('-created_at')
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


class TagView(APIView):
    def get(self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

    def post(self, request):
        serilizer = TagSerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data, status=status.HTTP_201_CREATED)
        return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class FeedbackView(APIView):
    def post(self, request):
        received_data = request.data
        received_data['name'] = request.user.id
        serializer = FeedbackSerializer(data=received_data)
        print(f"[DEBUG]: {request.data}")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StatView(APIView):
    def get(self, request):
        stats = Stat.objects.all()
        serializer = StatSerializer(stats, many=True)
        return Response(serializer.data)


class GalleryView(APIView):
    def get(self, request):
        gallery_items = GalleryItem.objects.all()
        serializer = GalleryItemSerializer(gallery_items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GalleryItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        gallery_items = GalleryItem.objects.all()
        gallery_items.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ResearchView(APIView):
    def get(self, request):
        research_cards = ResearchCard.objects.all()
        serializer = ResearchCardSerializer(research_cards, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ResearchCardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        research_cards = ResearchCard.objects.all()
        research_cards.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class AlumniView(APIView):
    def get(self, request):
        alumni_cards = AlumniCard.objects.all()
        serializer = AlumniCardSerializer(alumni_cards, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AlumniCardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        alumni_cards = AlumniCard.objects.all()
        alumni_cards.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class TimeLineView(APIView):
    def get(self, request):
        timeline_items = TimeLineItem.objects.all()
        serializer = TimeLineItemSerializer(timeline_items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TimeLineItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        timeline_items = TimeLineItem.objects.all()
        timeline_items.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class FacultyCardView(APIView):
    def get(self, request):
        faculty_cards = FacultyCard.objects.all()
        serializer = FacultyCardSerializer(faculty_cards, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FacultyCardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        faculty_cards = FacultyCard.objects.all()
        faculty_cards.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class PostView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        posts = Post.objects.all()
        posts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

