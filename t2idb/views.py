from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import text2image
from .serializers import IslImageSerializer

# Create your views here.


@api_view()
def isl_images_list(request):
    queryset = text2image.objects.all()
    serializer = IslImageSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def individual_isl_image(request, id):
    character = get_object_or_404(text2image, pk=id)
    serializer = IslImageSerializer(character)
    return Response(serializer.data)
