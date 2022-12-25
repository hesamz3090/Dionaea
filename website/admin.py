from django.contrib import admin
from .models import *


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super(ProfileAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    list_display = ('id', 'user')
    search_fields = ('id', 'user')


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super(SettingAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    list_display = ('id', 'user')
    search_fields = ('id', 'user')


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
