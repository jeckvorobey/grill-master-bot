from django.db import models
from django.utils import timezone

from apps.users.models import User
from utils.models import CreateUpdateTracker


class ActiveAddressManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(deleted_at__isnull=True)


class Address(CreateUpdateTracker):
	id = models.BigAutoField(primary_key=True, verbose_name='ID')
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Пользователь')
	address = models.CharField(max_length=255, verbose_name='Адрес')
	name = models.CharField(max_length=100, null=True, verbose_name='Название')
	
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
