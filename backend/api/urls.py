from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from . import views


urlpatterns = [
    path('verify/', views.VerifyEmailView.as_view(), name='verify-email'),
    path('login/', views.CustomLoginView.as_view(), name='api-login'),
    path('register/', views.CustomUserCreate.as_view(), name='api-register'),
    path('logout/', views.CustomLogoutView.as_view(), name='api-logout'),
    path('departments/', views.DepartmentListView.as_view(), name='department-list'),
    path('departments/<int:serial_number>/', views.DepartmentDetailView.as_view(), name='department-detail'),
    path('faculties/', views.FacultyListView.as_view(), name='faculty-list'),
    path('faculties/<int:faculty_id>/', views.FacultyDetailView.as_view(), name='faculty-detail'),
    path('blogs/', views.BlogListView.as_view(), name='blog-list'),
    path('blogs/<int:blog_id>/', views.BlogDetailView.as_view(), name='blog-detail'),
    path('comments/', views.CommentListView.as_view(), name='comment-list'),
    path('comments/<int:comment_id>/', views.CommentDetailView.as_view(), name='comment-detail'),
    path('events/', views.EventListView.as_view(), name='event-list'),
    path('events/<int:event_id>/', views.EventDetailView.as_view(), name='event-detail'),
    path('notices/', views.NoticeListView.as_view(), name='notice-list'),
    path('notices/<int:notice_id>/', views.NoticeDetailView.as_view(), name='notice-detail'),
    
]