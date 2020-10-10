from rest_framework import status, viewsets
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all().order_by('name')
    parser_classes = [MultiPartParser]