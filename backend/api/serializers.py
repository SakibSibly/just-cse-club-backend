from rest_framework import serializers
from .models import CustomUser, Department, Faculty, Blog, Comment, Event, Notice, Feedback, Tag, Stat, GalleryItem, ResearchCard, AlumniCard, TimeLineItem, FacultyCard, Post, Treasury, EventRegistration



class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'city']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class EventRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventRegistration
        fields = '__all__'


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = '__all__'


class GalleryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryItem
        fields = '__all__'


class ResearchCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchCard
        fields = '__all__'


class AlumniCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlumniCard
        fields = '__all__'


class TimeLineItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeLineItem
        fields = '__all__'


class FacultyCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacultyCard
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class TreasurySerializer(serializers.ModelSerializer):
    class Meta:
        model = Treasury
        fields = '__all__'