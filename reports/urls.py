from django.urls import path
from .views import StudentPerformanceReport, ScheduleReport

urlpatterns = [
    path('student/<int:pk>/', StudentPerformanceReport.as_view(), name='student-performance-report'),
    path('class/<int:pk>/', ScheduleReport.as_view(), name='class-schedule-report'),
]