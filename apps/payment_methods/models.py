from django.db import models

from utils.models import CreateUpdateTracker


class PaymentMethod(CreateUpdateTracker):
    id = models.BigAutoField(primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    label = models.CharField(max_length=100, verbose_name='Метка')

    class Meta:
        verbose_name = 'Способ оплаты'
        verbose_name_plural = 'Способы оплаты'

    def __str__(self):
        return self.label
