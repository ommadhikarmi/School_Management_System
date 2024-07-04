
from django.urls import path
from .views import ClassView,EnrollmentView

class_list = ClassView.as_view({
    'get':'list',
    'post':'create'
    })
class_details = ClassView.as_view({
    'get':'retrieve',
    'put':'update',
    'delete':'destroy'
    })

enrollment_list = EnrollmentView.as_view({
    'get':'list',
    'post':'create'
    })
enrollment_details = EnrollmentView.as_view({
    'get':'retrieve',
    'put':'update',
    'delete':'destroy'
    })

urlpatterns = [
    path('classes/',class_list, name='class_list'),
    path('classes/<int:pk>/',class_details, name='class_details'),

    path('enrollments/',enrollment_list, name='enrollment_list'),
    path('enrollments/<int:pk>/',enrollment_details, name='enrollment_details'),
]
