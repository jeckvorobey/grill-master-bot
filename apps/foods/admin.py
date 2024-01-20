from django.contrib import admin
from .models import Food


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
	list_display = ['category', 'type', 'name', 'image', 'description', 'cost']
