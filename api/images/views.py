# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import status
from rest_framework.parsers import FileUploadParser, JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Image, ImageSearch
from .serializers import ImageSerializer

# Create your views here.


class ImagesView(APIView):
    parser_class = (FileUploadParser, JSONParser)

    def post(self, request, *args, **kwargs):
        file_serializer = ImageSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response({'images': serializer.data}, status=status.HTTP_200_OK)


class OneImageView(APIView):
    parser_class = (JSONParser)

    def get(self, request, pk):
        image = Image.objects.filter(id=pk)
        serializer = ImageSerializer(image, many=True)
        return Response({'image': serializer.data}, status=status.HTTP_200_OK)


class SearchView(APIView):

    def get(self, request, pk):
        image = Image.objects.filter(id=pk)
        search = ImageSearch(client=request.headers['User-Agent'])

        return Response(status=status.HTTP_200_OK)
