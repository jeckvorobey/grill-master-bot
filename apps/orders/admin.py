from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'status', 'payment_method', 'price', 'add_info')
	list_filter = ('status', 'payment_method')
	search_fields = ('user__username', 'add_info')
	raw_id_fields = ('user',)
