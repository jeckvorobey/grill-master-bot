from rest_framework import serializers

from .models import Food
from ..categories.models import Category


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
