from django.contrib import admin

from .models import Electronic, Category


class ElectronicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = list_display


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = list_display


admin.site.register(Electronic)
admin.site.register(Category)
