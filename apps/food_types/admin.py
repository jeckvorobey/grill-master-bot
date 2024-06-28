from django.contrib import admin
from .models import FoodType


@admin.register(FoodType)
class FoodTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'label', 'created_at', 'updated_at']
