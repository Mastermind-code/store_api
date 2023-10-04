from django.contrib import admin
from django.urls import path
from .views import get_products, get_product
urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', get_products, name='get_all_products'),
    path('products/<str:pk>', get_product, name='get_product')
]
