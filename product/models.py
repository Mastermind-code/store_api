from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.TextChoices):
    electronics = 'Electronics'
    Laptop = 'Laptop'
    Accessories = 'Accessories'
    Food = 'Food'
    Home = 'Home'


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=250)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    stock = models.IntegerField()
    category = models.CharField(choices=Category.choices, max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name