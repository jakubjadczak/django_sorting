from django.db import models
from sorl.thumbnail import ImageField


def upload_to(filename):
    return f'django_algorytmy/media/{filename}'


class Image(models.Model):
    chart = ImageField(verbose_name='wykres', upload_to=upload_to)
    data = models.DateField(auto_now=True)