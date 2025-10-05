#new import
from django.urls import path
    # SMSApp/urls.py
from django.urls import path
from .views import StudentListAPI, StudentCreateAPI, StudentDetailAPI, StudentUpdateAPI, StudentDeleteAPI


urlpatterns = [
    path('students/', StudentListAPI.as_view(), name='student-list'),
    path('students/create/', StudentCreateAPI.as_view(), name='student-create'),
    path('students/<int:pk>/', StudentDetailAPI.as_view(), name='student-detail'),
    path('students/<int:pk>/update/', StudentUpdateAPI.as_view(), name='student-update'),
    path('students/<int:pk>/delete/', StudentDeleteAPI.as_view(), name='student-delete'),
]