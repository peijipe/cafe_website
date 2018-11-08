from django.contrib import admin
from .models import Reserve, Customer, Course, Status, Res


class ReserveAdmin(admin.ModelAdmin):
    admin.site.register(Reserve)


class Customer(admin.ModelAdmin):
    admin.site.register(Customer)


class Course(admin.ModelAdmin):
    admin.site.register(Course)


class Status(admin.ModelAdmin):
    admin.site.register(Status)


class ReserveAdmin(admin.ModelAdmin):
    admin.site.register(Res)
