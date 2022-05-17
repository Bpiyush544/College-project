from django.urls import path
from . views import AddMoney, ProductDetailView, ProductListView, UpdateProductView, account, accountHolderView, historyView, home, AddProductView, contact
from . views import home

urlpatterns = [
    path('', home, name="home"),
    path('contact/', contact, name="contact"),
    path('add_product/', AddProductView.as_view(), name="add_product"),
    path('product_list/', ProductListView, name="product_list"),
    path('product_list/product_display/<str:name>/',
         ProductDetailView, name="product_detail"),
    path('accountHolders/', accountHolderView, name="accountHolders"),
    path('accountHolders/<str:cus>', account, name="account"),
    path('history/<str:mssg>', historyView, name="history"),
    path('add_money/<str:user>', AddMoney, name="add_money"),
    path('product_list/product_update/<int:pk>',
         UpdateProductView.as_view(), name="product_update"),
]
