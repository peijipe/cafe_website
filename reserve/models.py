from django.db import models


class Reserve(models.Model):
    name = models.ForeignKey('Customer', on_delete=models.CASCADE)
    datetime = models.DateTimeField(blank=False)
    num = models.IntegerField(blank=False)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    comment = models.CharField(blank=False, max_length=1000)
    status = models.ForeignKey('Status', on_delete=models.CASCADE)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_id


class Customer(models.Model):
    name = models.CharField(max_length=150)
    tel = models.CharField(max_length=13)
    mail = models.EmailField()
    password = models.CharField(max_length=20)
    comment = models.CharField(max_length=1000)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=150)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Status(models.Model):
    status = models.CharField(max_length=150)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status
