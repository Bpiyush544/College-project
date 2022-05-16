from django import forms
from . models import Product


products = Product.objects.all().values_list('name', 'name')

choice_list = []

for product in products:
    choice_list.append(product)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'display_name',
                  'price', 'description', 'image')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'display_name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }


class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('display_name', 'price', 'description', 'image')
        widgets = {
            'display_name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }
