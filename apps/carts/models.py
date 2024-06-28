from django.db import models
from apps.users.models import User
from apps.foods.models import Food
from utils.models import CreateUpdateTracker


class Cart(CreateUpdateTracker):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart', verbose_name='Пользователь')
	foods = models.ManyToManyField(Food, through='CartFood', verbose_name='Блюда')

	class Meta:
		verbose_name = 'Корзина'
		verbose_name_plural = 'Корзины'
	
	def __str__(self):
		return f"Cart of {self.user.username}"


class CartFood(models.Model):
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='Корзина')
	food = models.ForeignKey(Food, on_delete=models.CASCADE, verbose_name='Блюдо')
	quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

	class Meta:
		verbose_name = 'Блюдо в Корзине'
		verbose_name_plural = 'Блюда в Корзине'
	
	def __str__(self):
		return f"{self.quantity} x {self.food.name} in {self.cart}"
