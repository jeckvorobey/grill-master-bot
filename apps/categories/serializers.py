from rest_framework import serializers
from apps.categories.models import Category
from apps.foods.models import Food
from apps.foods.serializers import FoodSerializer


class CategorySerializer(serializers.ModelSerializer):
    foods = FoodSerializer(many=True, read_only=True, source='food_set')

    class Meta:
        model = Category
        fields = ['id', 'name', 'icon', 'foods']
