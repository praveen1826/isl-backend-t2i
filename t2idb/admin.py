from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.text2image)
class text2imageAdmin(admin.ModelAdmin):
    list_display = ['character', 'image']
    list_editable = ['image']
    ordering = ['character']
    search_fields = ['character']
