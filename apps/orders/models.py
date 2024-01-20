from django.db import models

from apps.foods.models import Food
from apps.payment_methods.models import PaymentMethod
from apps.statuses.models import Status
from apps.users.models import User
from utils.models import CreateUpdateTracker


class Order(CreateUpdateTracker):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
	payment_method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True)
	price = models.FloatField()
	sale = models.IntegerField(null=True, blank=True)
	add_info = models.TextField(null=True, blank=True)
	foods = models.ManyToManyField(Food, through='FoodOrder')
	
	def __str__(self):
		return f'Заказ {self.id} от {self.user}'


class FoodOrder(models.Model):
	food = models.ForeignKey(Food, on_delete=models.CASCADE)
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	
	def __str__(self):
		return f'{self.food.name} в Заказе {self.order.id}'
