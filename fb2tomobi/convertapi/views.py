from django.shortcuts import render
from rest_framework import parsers, response, viewsets, status
from .serializers import BookFileSerializer, BookSerializer
from .models import Book
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all().order_by('name')
    parser_classes = [JSONParser]
    def post(self, request, format=None):
        return response.Response({'received data': request.data})
    # @action(
    #     detail=True,
    #     methods=['PUT'],
    #     serializer_class=BookFileSerializer,
    #     parser_classes=[parsers.MultiPartParser],
    # )
    # def book(self, request, pk):
    #     obj = self.get_object()
    #     serializer = self.serializer_class(obj, data=request.data,
    #                                        partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return response.Response(serializer.data)
    #     return response.Response(serializer.errors,
    #                              status.HTTP_400_BAD_REQUEST)
    # queryset = Book.objects.all().order_by('name')
    # serializer_class = BookSerializer
