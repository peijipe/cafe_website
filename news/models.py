from django.db import models
from stdimage.models import StdImageField


class Post(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField(blank=True)
    image = StdImageField(upload_to='picture/news', blank=True, variations={
        'large': (600, 400),
        'thumbnail': (100, 100, True),
        'medium': (300, 200),
    })
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

