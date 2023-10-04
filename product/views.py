from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilters


# Create your views here.
@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()

    filters = ProductFilters(request.GET, queryset=products.order_by('id'))
    rss_per_page = 1
    paginator = PageNumberPagination()
    paginator.page_size = rss_per_page
    queryset = paginator.paginate_queryset(filters.qs, request)
    serializer = ProductSerializer(queryset, many=True)

    context = {
        'product': serializer.data
    }
    return Response(context)


@api_view(['GET'])
def get_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    serializer = ProductSerializer(product)

    context = {
        'product': serializer.data
    }

    return Response(context)
