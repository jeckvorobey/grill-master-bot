from django.core.exceptions import ObjectDoesNotExist
from django.db import models

nb = dict(null=True, blank=True)


class CreateTracker(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Создан')

    class Meta:
        abstract = True
        ordering = ('-created_at',)


class CreateUpdateTracker(CreateTracker):
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')

    class Meta(CreateTracker.Meta):
        abstract = True


class GetOrNoneManager(models.Manager):
    """returns none if object doesn't exist else model instance"""

    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except ObjectDoesNotExist:
            return None


# Добавляем менеджер моделей для мягкого удаления
class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        """Returns queryset excluding soft-deleted objects."""
        return super().get_queryset().filter(is_deleted=False)


# Добавляем модель трекера, которая поддерживает мягкое удаление
class CreateUpdateSoftDeleteTracker(CreateUpdateTracker):
    is_deleted = models.BooleanField(default=False, verbose_name='Удален')

    objects = SoftDeleteManager()  # Updating the default manager to SoftDeleteManager
    all_objects = models.Manager()  # Keep original manager to access all objects including soft-deleted

    class Meta(CreateUpdateTracker.Meta):
        abstract = True

    def delete(self, *args, **kwargs):
        """Soft delete the object."""
        self.is_deleted = True
        self.save()

    def hard_delete(self, *args, **kwargs):
        """Completely removes the object from the database."""
        super().delete(*args, **kwargs)
