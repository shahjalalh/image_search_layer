from rest_framework import serializers
from imagesearch_app.models import Image, ImageSearch

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('url', 'snippet', 'thumbnail', 'context')


class ImageSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageSearch
        fields = ('term', 'when')
