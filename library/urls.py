from django.urls import path
from .views import BookView,BorrowRecordView

book_list = BookView.as_view({
    'get': 'list',
    'post': 'create'
})
book_detail = BookView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

borrow_record_list = BorrowRecordView.as_view({
    'get': 'list',
    'post': 'create'
})
borrow_record_detail = BorrowRecordView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path('books/', book_list, name='book-list'),
    path('books/<int:pk>/', book_detail, name='book-detail'),
    path('borrow-records/', borrow_record_list, name='borrowrecord-list'),
    path('borrow-records/<int:pk>/', borrow_record_detail, name='borrowrecord-detail'),
]
