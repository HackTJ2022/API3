from rest_framework import serializers

from .models import MyFile


class ImageRecognitionSerializer(serializers.ModelSerializer):
    class Meta():
        model = MyFile
        fields = ('file',)
