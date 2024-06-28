from django.db import models

from utils.models import CreateUpdateTracker


class Status(CreateUpdateTracker):
    id = models.BigAutoField(primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    label = models.CharField(max_length=100, verbose_name='Метка')

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.label
