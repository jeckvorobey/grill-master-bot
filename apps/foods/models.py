from django.db import models

from apps.categories.models import Category
from apps.food_types.models import FoodType
from utils.models import CreateUpdateTracker


class Food(CreateUpdateTracker):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='foods/', blank=True, null=True)
    cost = models.FloatField()

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(FoodType, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.image:
            self.image = 'default/no-photo.png'
        super().save(*args, **kwargs)
