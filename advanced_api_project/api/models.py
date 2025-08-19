from django.db import models

# Create your models here.

class Author(models.Model):
    """Model representing an author., has a name field."""
    name = models.CharField(max_length=100)

class Book(models.Model):
    """Model representing a book, has a title, author, and publication year."""
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    publication_year = models.IntegerField()    