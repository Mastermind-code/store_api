from django_filters import rest_framework as filters
from .models import Product


class ProductFilters(filters.FilterSet):
    keyword = filters.CharFilter(field_name='name', lookup_expr='contains')
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')


    class Meta:
        model = Product
        fields = ('keyword', "min_price", 'max_price','name', 'category')
