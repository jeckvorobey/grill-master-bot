from django.db import models

from utils.models import CreateUpdateTracker


class Category(CreateUpdateTracker):
	id = models.BigAutoField(primary_key=True, verbose_name='ID')
	name = models.CharField(max_length=255, verbose_name='Наименование')
	label = models.CharField(max_length=255, verbose_name='Метка')
	is_active = models.BooleanField(default=True, verbose_name='Активен')

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

	def __str__(self):
		return self.label

