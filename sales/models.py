from django.db import models
from django.utils import timezone


class Sale(models.Model):
	id = models.BigAutoField(primary_key=True)
	label = models.CharField(max_length=255)
	value = models.IntegerField(help_text="Скидка в процентах")
	update_at = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add=True)
	deleted_at = models.DateTimeField(blank=True, null=True)
	
	def __str__(self):
		return self.label
