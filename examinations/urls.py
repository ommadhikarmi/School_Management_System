
from django.urls import path
from .views import ExaminationView,GradeView

Examination_list = ExaminationView.as_view({
    'get':'list',
    'post':'create'
    })
examination_details = ExaminationView.as_view({
    'get':'retrieve',
    'put':'update',
    'delete':'destroy'
    })

grade_list = GradeView.as_view({
    'get':'list',
    'post':'create'
    })
grade_details = GradeView.as_view({
    'get':'retrieve',
    'put':'update',
    'delete':'destroy'
    })

urlpatterns = [
    path('examination/',Examination_list, name='examination_list'),
    path('examination/<int:pk>/',examination_details, name='examination_details'),

    path('grade/',grade_list, name='grade_list'),
    path('grade/<int:pk>/',grade_details, name='grade_details'),
]
