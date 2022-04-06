from unicodedata import name
from django.urls import path
from . views import ProductDetailView, ProductListView, account, accountHolderView, historyView, home, AddProductView
from . views import home

urlpatterns = [
    path('', home, name="home"),
    path('add_product/', AddProductView, name="add_product"),
    path('product_list/', ProductListView, name="product_list"),
    path('product_list/product_display/<int:pk>/',
         ProductDetailView, name="product_detail"),
    path('accountHolders/', accountHolderView, name="accountHolders"),
    path('accountHolders/<str:cus>', account, name="account"),
    path('history/<str:mssg>', historyView, name="history")
]
