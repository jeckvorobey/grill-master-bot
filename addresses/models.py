from django.db import models
from django.utils import timezone

from users.models import User


class ActiveAddressManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(deleted_at__isnull=True)


class Address(models.Model):
	id = models.BigAutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	address = models.CharField(max_length=255)
	name = models.CharField(max_length=100, null=True)
	update_at = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add=True)
	deleted_at = models.DateTimeField(blank=True, null=True)
	
	# Объект с не удалёнными адресами
	objects = ActiveAddressManager()
	# Все объекты
	all_objects = models.Manager()
	
	def __str__(self):
		return self.name
	
	def soft_delete(self):
		self.deleted_at = timezone.now()
		self.save()
	
	def is_deleted(self):
		return self.deleted_at is not None
	
	def delete(self, using=None, keep_parents=False):
		self.soft_delete()
