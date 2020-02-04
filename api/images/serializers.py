from rest_framework import serializers

from .models import Image, ImageResult, ImageSearch

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class ImageResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageResult
        fields = '__all__'

class ImageSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageSearch
        fields = '__all__'