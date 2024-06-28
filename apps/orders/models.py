from django.db import models

from apps.foods.models import Food
from apps.payment_methods.models import PaymentMethod
from apps.statuses.models import Status
from apps.users.models import User
from utils.models import CreateUpdateTracker


class Order(CreateUpdateTracker):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Пользователь')
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, verbose_name='Статус')
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True,
                                       verbose_name='Способ оплаты')
    price = models.FloatField(verbose_name='Стоимость')
    sale = models.IntegerField(null=True, blank=True, verbose_name='скидка')
    add_info = models.TextField(null=True, blank=True, verbose_name='дополнительная информация')
    foods = models.ManyToManyField(Food, through='FoodOrder', verbose_name='Блюда')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ {self.id} от {self.user}'


class FoodOrder(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, verbose_name='Блюдо')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заявка')

    class Meta:
        verbose_name = 'Блюдо в Заказе'
        verbose_name_plural = 'Блюда в Заказе'

    def __str__(self):
        return f'{self.food.name} в Заказе {self.order.id}'
