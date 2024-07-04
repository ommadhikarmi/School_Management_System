from django.urls import path
from .views import Academic_RecordView

academic_record_list = Academic_RecordView.as_view({
    'get':'list',
    'post':'create'
    })
academic_record_details = Academic_RecordView.as_view({
    'get':'retrieve',
    'put':'update',
    'delete':'destroy'
    })


urlpatterns = [
    path('academic_records/',academic_record_list, name='academic_record'),
    path('academic_records/<int:pk>/',academic_record_details, name='academic_record_details'),
]