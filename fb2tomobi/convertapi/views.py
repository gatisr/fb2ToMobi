from rest_framework import status, viewsets
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
import subprocess
import os
from django.conf import settings
from .models import Book
from .serializers import BookSerializer
from django.core.files.base import ContentFile

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all().order_by('name')
    parser_classes = [MultiPartParser]
    http_method_names = ['get', 'put', 'delete']
    def put(self, request, *args, **kwargs):
        file_serializer = BookSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            book_name = file_serializer.root.data["book"]
            file_to_convert = book_name.replace(settings.MEDIA_URL, settings.MEDIA_ROOT + '\\')
            new_file_location = os.path.splitext(file_to_convert)[0] + '.mobi'
            final_convert_command = settings.CALIBRE_CONVERTER_LOCATION + " " + file_to_convert + " " + new_file_location
            subprocess.check_call(final_convert_command)
            created_book = Book.objects.filter(pk=file_serializer.root.data["pk"]).first()
            with open(file_to_convert, "rb") as fh:
                with ContentFile(fh.read()) as 	file_content:
                    created_book.converted_book.save(os.path.splitext(book_name.replace(settings.MEDIA_URL,''))[0]+'.mobi', file_content)
                    created_book.save()
            return Response(BookSerializer(created_book).data, status=status.HTTP_201_CREATED)
        else:
            return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)