from rest_framework import status, viewsets
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all().order_by('name')
    parser_classes = [MultiPartParser]

    def post(self, request):
        file = request.data.get('book')
        if file and not file.name.endswith('.fb2'):
            return Response({'errors': "file type is not supported"}, status=400)
        file_serializer = BookSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
