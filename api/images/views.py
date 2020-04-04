# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from rest_framework import status
from rest_framework.parsers import FileUploadParser, JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Image
from .serializers import ImageSerializer, ImageResultSerializer

from cnn.query_online import get_result


# Create your views here.

# /images
# @post : permet d'upload une image provenant de l'application Android
# @get : permet de retourner toutes les images qui ont été postées
class ImagesView(APIView):
    #parser_class = (FileUploadParser, JSONParser)

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


# /images/<id>
# @get : permet de retourner une seule image via son <id> qui a été uploadée
class OneImageView(APIView):
    # parser_class = (JSONParser)

    def get(self, request, pk):
        image = Image.objects.filter(id=pk)
        serializer = ImageSerializer(image, many=True)
        return Response({'images': serializer.data}, status=status.HTTP_200_OK)


# /images/result
# @get : permet de retourner le top 5 des images CNN associée à la dernière image uploadée
class ImagesResultView(APIView):

    def get(self, request):
        get_img = Image.objects.last()
        images = get_result(str(get_img))
        serializer = ImageResultSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
