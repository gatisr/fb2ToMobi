from rest_framework import status, viewsets
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
import subprocess
import os
from django.conf import settings
from .models import Book
from .serializers import BookSerializer, BookSerializerPost
from django.core.files.base import ContentFile

CONVERT_TO_EXTENSION = '.mobi'

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('pk')
    parser_classes = [MultiPartParser]
    http_method_names = ['get', 'put', 'delete']

    def get_serializer_class(self):
        is_post_request = self.request.method == 'POST'
        is_post_form = self.action == None or self.action == 'update'
        if is_post_request or is_post_form:
            return BookSerializerPost
        return BookSerializer

    def put(self, request):
        file_serializer = BookSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            book_name = file_serializer.root.data["book"].replace(settings.MEDIA_URL, '')
            book_name_mobi = os.path.splitext(book_name)[0] + CONVERT_TO_EXTENSION
            file_to_convert = settings.MEDIA_ROOT + '\\' + book_name
            new_file_location = settings.MEDIA_ROOT + '\\' + book_name_mobi
            final_convert_command = settings.CALIBRE_CONVERTER_LOCATION + " " + file_to_convert + " " + new_file_location
            subprocess.check_call(final_convert_command)
            created_book = Book.objects.filter(pk=file_serializer.root.data["pk"]).first()
            with open(file_to_convert, "rb") as fh:
                with ContentFile(fh.read()) as 	file_content:
                    created_book.converted_book.name = book_name_mobi
                    created_book.save()
            return Response(BookSerializer(created_book).data, status=status.HTTP_201_CREATED)
        else:
            return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)