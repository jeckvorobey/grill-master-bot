from rest_framework import generics

from .models import Food
from .serializers import FoodSerializer
from ..categories.models import Category


# Create your views here.
class FoodsApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = FoodSerializer
