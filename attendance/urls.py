from django.urls import path
from .views import AttendanceView

attendance_list = AttendanceView.as_view({
    'get':'list',
    'post':'create'
    })
attendance_details = AttendanceView.as_view({
    'get':'retrieve',
    'put':'update',
    'delete':'destroy'
    })


urlpatterns = [
    path('attendances/',attendance_list, name='attendance_list'),
    path('attendances/<int:pk>/',attendance_details, name='attendance_details'),
]