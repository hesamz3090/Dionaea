from django.contrib import admin
from .models import *


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'descriptions', 'url', 'created_on', 'updated_on', 'author')
    list_filter = ('created_on', 'updated_on', 'author')
    search_fields = ('id', 'name')

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()
