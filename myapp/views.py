# myapp/views.py

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from django.views.generic import ListView, DetailView


# -- API Views --

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# -- Template Views --

class BookListView(ListView):
    model = Book
    template_name = 'myapp/book_list.html'  # in templates/myapp/book_list.html
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'myapp/book_detail.html'  # in templates/myapp/book_detail.html
    context_object_name = 'book'