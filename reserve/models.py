from django.db import models


class Res(models.Model):
    name = models.CharField(blank=False, max_length=20)
    datetime = models.DateTimeField(blank=False)
    num = models.IntegerField(blank=False)
    course = models.CharField(max_length=150)
    comment = models.CharField(blank=True, max_length=1000)

    def __str__(self):
        return self.name
