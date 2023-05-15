from rest_framework import serializers
from .models import text2image


class IslImageSerializer(serializers.Serializer):
    character = serializers.CharField(max_length=10)
    image = serializers.ImageField()
