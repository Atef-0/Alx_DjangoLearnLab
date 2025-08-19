from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    
    """Serializer for the Book model."""
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
    
    """Validate publication year to ensure it is not in the future."""
    def validate(self, attrs):
        if attrs['publication_year'] > datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return attrs
    

class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for the Author model, includes related books."""
    
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['name', 'books']

    