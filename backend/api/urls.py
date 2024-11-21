from django.urls import path
from . import views


urlpatterns = [
    path('department/', views.DepartmentListView.as_view(), name='department-list'),
    path('department/<int:serial_number>/', views.DepartmentDetailView.as_view(), name='department-detail'),
    path('faculty/', views.FacultyListView.as_view(), name='faculty-list'),
    path('faculty/<int:faculty_id>/', views.FacultyDetailView.as_view(), name='faculty-detail'),
]