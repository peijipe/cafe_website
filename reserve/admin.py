from django.contrib import admin
from .models import Res


class ReserveAdmin(admin.ModelAdmin):
    admin.site.register(Res)
