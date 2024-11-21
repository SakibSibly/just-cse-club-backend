from django.urls import path
from . import views


urlpatterns = [
    path('departments/', views.DepartmentListView.as_view(), name='department-list'),
    path('departments/<int:department_id>/', views.DepartmentDetailView.as_view(), name='department-detail'),
    path('faculty/', views.FacultyListView.as_view(), name='faculty-list'),
    path('faculty/<int:faculty_id>/', views.FacultyDetailView.as_view(), name='faculty-detail'),
]