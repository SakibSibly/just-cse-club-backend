from django.urls import path
from . import views


urlpatterns = [
    path('departments/', views.DepartmentListView.as_view(), name='department-list'),
    path('departments/<int:serial_number>/', views.DepartmentDetailView.as_view(), name='department-detail'),
    path('faculties/', views.FacultyListView.as_view(), name='faculty-list'),
    path('faculties/<int:faculty_id>/', views.FacultyDetailView.as_view(), name='faculty-detail'),
]