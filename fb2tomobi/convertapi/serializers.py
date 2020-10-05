from rest_framework import serializers

from .models import Book

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'book', 'uploadedAt')
        read_only_fields = ['book']

class BookFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['book']