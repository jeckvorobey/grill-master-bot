from rest_framework import viewsets

from apps.categories.models import Category
from apps.categories.serializers import CategorySerializer


# Create your views here.
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
