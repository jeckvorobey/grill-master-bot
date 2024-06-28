from django.db import models

from apps.categories.models import Category
from apps.food_types.models import FoodType
from utils.models import CreateUpdateTracker, nb


class Food(CreateUpdateTracker):
    id = models.BigAutoField(primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(**nb, verbose_name='Описание')
    image = models.ImageField(upload_to='foods/', **nb, verbose_name='Изображение')
    cost = models.FloatField(verbose_name='Стоимость')

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Категория')
    type = models.ForeignKey(FoodType, on_delete=models.SET_NULL, null=True, verbose_name='Тип')

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.image:
            self.image = 'default/no-photo.png'
        super().save(*args, **kwargs)
