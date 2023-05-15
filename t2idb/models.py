from django.db import models

# Create your models here.


class text2image(models.Model):
    character = models.CharField(max_length=10, primary_key=True)
    image = models.ImageField(upload_to='images')

    def __str__(self) -> str:
        return self.character
