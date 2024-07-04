from django.urls import path
from .views import TeacherView

teacher_list = TeacherView.as_view({
    'get':'list',
    'post':'create'
    })
teacher_details = TeacherView.as_view({
    'get':'retrieve',
    'put':'update',
    'delete':'destroy'
    })


urlpatterns = [
    path('',teacher_list, name='teacher_list'),
    path('<int:pk>/',teacher_details, name='teacher_details'),
]