from django.shortcuts import render
from django.http import HttpResponse
from t2idb.models import text2image

# Create your views here.


def txt2img(request):
    query_set = text2image.objects.get(pk='d')

    return render(request, 'text2image.html')
