from django.urls import path
from .views import StudentView

student_list = StudentView.as_view({
    'get':'list',
    'post':'create'
    })
student_details = StudentView.as_view({
    'get':'retrieve',
    'put':'update',
    'delete':'destroy'
    })


urlpatterns = [
    path('',student_list, name='student_list'),
    path('<int:pk>/',student_details, name='student_details'),
]