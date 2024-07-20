from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'icon', 'name', 'label', 'img', 'is_active', 'created_at', 'updated_at']
