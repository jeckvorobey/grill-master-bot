from django.contrib import admin

from .models import Cart, CartFood


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'foods_display']
    ordering = ['user']

    def foods_display(self, obj):
        return ", ".join([food.name for food in obj.foods.all()])

    foods_display.short_description = "Блюда"


@admin.register(CartFood)
class CartFoodAdmin(admin.ModelAdmin):
    list_display = ['cart', 'food', 'quantity']
    ordering = ['cart']
