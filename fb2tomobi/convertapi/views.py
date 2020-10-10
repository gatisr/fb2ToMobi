from django.shortcuts import render
from rest_framework import parsers, response, viewsets, status
from .serializers import BookSerializer
from .models import Book
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser, MultiPartParser  


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all().order_by('name')

    parser_classes = [MultiPartParser]
