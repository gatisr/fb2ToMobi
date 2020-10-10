from rest_framework import serializers
from .models import Book
from django.core.files.uploadedfile import InMemoryUploadedFile

class BookSerializer(serializers.ModelSerializer):

    def validate_book(self, book: InMemoryUploadedFile) -> InMemoryUploadedFile:
        if not book or not book.name.endswith('.fb2'):
            raise serializers.ValidationError('file type is not supported!')
        return book

    class Meta:
        model = Book
        fields = ('pk', 'name', 'book', 'uploaded_at', 'converted_book')
