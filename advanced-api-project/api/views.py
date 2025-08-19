from django.shortcuts import render
from rest_framework import generics
from django.urls import reverse_lazy
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
import django_filters.rest_framework
from rest_framework import filters
from django_filters import rest_framework


# Create your views here.
"""
Implement a set of generic views for the Book model to handle CRUD operations. This includes:
-A ListView for retrieving all books.
-A DetailView for retrieving a single book by ID.
-A CreateView for adding a new book.
-An UpdateView for modifying an existing book.
-A DeleteView for removing a book
"""

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'published_date']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    success_url = reverse_lazy('book-list')
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return self.get_success_response(serializer.data)
        return self.get_error_response(serializer.errors)

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'
    success_url = reverse_lazy('book-list')
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return self.get_success_response(serializer.data)
        return self.get_error_response(serializer.errors)

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'
    success_url = reverse_lazy('book-list')
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return self.get_success_response({'message': 'Book deleted successfully'})