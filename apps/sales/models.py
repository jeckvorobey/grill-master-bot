from django.db import models

from utils.models import CreateUpdateSoftDeleteTracker


class Sale(CreateUpdateSoftDeleteTracker):
    id = models.BigAutoField(primary_key=True, verbose_name='ID')
    label = models.CharField(max_length=255, verbose_name='Метка')
    value = models.IntegerField(help_text="Скидка в процентах", verbose_name='Значение')

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'

    def __str__(self):
        return self.label
