# myapp/urls.py

from django.urls import path
from .views import (
    BookListCreateAPIView,
    BookRetrieveUpdateDestroyAPIView,
    BookListView,
    BookDetailView
)

urlpatterns = [
    # API endpoints
    path('api/books/', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('api/books/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='book-rud'),

    # Template views
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]