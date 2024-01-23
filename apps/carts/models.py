from django.db import models
from apps.users.models import User
from apps.foods.models import Food
from utils.models import CreateUpdateTracker


class Cart(CreateUpdateTracker):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
	foods = models.ManyToManyField(Food, through='CartFood')
	
	def __str__(self):
		return f"Cart of {self.user.username}"


class CartFood(models.Model):
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
	food = models.ForeignKey(Food, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=1)
	
	def __str__(self):
		return f"{self.quantity} x {self.food.name} in {self.cart}"
