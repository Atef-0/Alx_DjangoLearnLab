from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('books/<int:id>/', views.BookDetailView.as_view(), name='book-detail'),
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),
    path('books/update/<int:id>/', views.BookUpdateView.as_view(), name='book-update'),
    path('books/delete/<int:id>/', views.BookDeleteView.as_view(), name='book-delete'),
]