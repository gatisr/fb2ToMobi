from rest_framework import serializers
from .models import Book
from django.core.files.uploadedfile import InMemoryUploadedFile
import os

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('pk', 'name', 'book', 'uploaded_at', 'converted_book')
    def validate_book(self, book: InMemoryUploadedFile) -> InMemoryUploadedFile:
        if book is None or type(book) is not InMemoryUploadedFile:
            raise serializers.ValidationError('invalid file!')
        fileName, extension = os.path.splitext(book.name)
        if not book or extension.upper() not in SUPPORTED_FORMATS:
            raise serializers.ValidationError('file type is not supported!')
        return book

SUPPORTED_FORMATS = ['.FB2', '.EPUB', '.DOC', '.DOCX', '.PDF']
class BookSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('pk', 'name', 'book', 'uploaded_at')
