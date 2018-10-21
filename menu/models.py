from django.db import models
from stdimage.models import StdImageField


# class Category(models.Model):
#     category_name = models.CharField(max_length=150)
#     created_datetime = models.DateTimeField(auto_now_add=True)
#     updated_datetime = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.category_name


class Menu(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    image = StdImageField(upload_to='picture/menu', blank=True, variations={
        'thumbnail': (300, 225, True),
    })
    # category = models.ManyToManyField(Category)
    category = models.CharField(max_length=150, unique=False)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Course(models.Model):
    name = models.CharField(max_length=150)
    text = models.TextField(blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

