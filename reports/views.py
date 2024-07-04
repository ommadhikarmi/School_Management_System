from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from students.models import Student
from examinations.models import Grade
from attendance .models import Attendance
from classes.models import Class
from rest_framework.response import Response
# Create your views here.

class StudentPerformanceReport(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request,pk):
        student = Student.objects.get(id=pk)
        grades = Grade.objects.filter(student=student)
        attendance = Attendance.objects.filter(student=student)

        report = {
            "student":student.user.Username,
            "grades": [{"examination":grade.examination.name,
                         "grade":grade.grade} for grade in grades],
                         
                       
            "attendance": [{"date": att.date,
                             "status": att.status} for att in attendance],   
        }
        return Response(report)
    
class ScheduleReport(APIView):
    permission_classes =[IsAuthenticated]

    def get(self,request,pk):
        class_event = Class.objects.get(id=pk)
        schedule = class_event.schedule
        
        report = {
            "class":class_event.name,
            "schedule":schedule,
        }
        return Response(report)