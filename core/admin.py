from django.contrib import admin
from core.models import *

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    class Meta:
        model=About