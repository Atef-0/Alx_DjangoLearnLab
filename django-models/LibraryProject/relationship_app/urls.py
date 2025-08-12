from django.urls import path
from .views import list_books, LibraryListView

urlpatterns = [ 
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryListView.as_view(), name='library_detail'),
]