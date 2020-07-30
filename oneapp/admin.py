from django.contrib import admin
from .models import Url


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    list_filter = ('short_url', 'original_url', )
    search_fields = ('short_url', 'original_url', )
    list_display = ('short_url', 'original_url', )
