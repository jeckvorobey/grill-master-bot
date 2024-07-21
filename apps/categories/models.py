from django.db import models

from utils.models import CreateUpdateTracker, nb


class Category(CreateUpdateTracker):
	id = models.BigAutoField(primary_key=True, verbose_name='ID')
	name = models.CharField(max_length=255, verbose_name='Наименование')
	label = models.CharField(max_length=255, verbose_name='Метка')
	img = models.ImageField(upload_to='images/categories/', verbose_name='Изображение', **nb)
	icon = models.CharField(max_length=100, verbose_name='Иконка', **nb)
	is_active = models.BooleanField(default=True, verbose_name='Активен')

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

	def __str__(self):
		return self.name

