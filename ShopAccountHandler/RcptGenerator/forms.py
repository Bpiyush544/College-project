from django.forms import forms
from . models import Product


products = Product.objects.all().values_list('name', 'name')

choice_list = []

for product in products:
    choice_list.append(product)
