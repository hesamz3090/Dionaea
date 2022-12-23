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


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'first_name', 'last_name', 'email', 'phone', 'type', 'subject', 'created_on')
    list_filter = ('type', 'subject', 'created_on')
    search_fields = ('id', 'title', 'first_name', 'last_name', 'email', 'phone', 'type', 'subject', 'created_on')
