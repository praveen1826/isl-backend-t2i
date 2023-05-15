from django.urls import path
from . import views

urlpatterns = [
    path("convert/", views.isl_images_list),
    path("convert/<id>/", views.individual_isl_image)
]
