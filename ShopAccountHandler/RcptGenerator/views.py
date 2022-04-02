import datetime
from django.shortcuts import render
from . models import Product, Receipt
from django.views.generic import CreateView
from django.contrib.auth.models import User


allUsers = User.objects.all()
customers = []

for user in allUsers:
    if(user.is_superuser == False):
        customers.append(user)


def home(request):
    return render(request, 'home.html')


def ProductListView(request):
    product_menu_list = Product.objects.all()
    print(product_menu_list[0].pk)
    return render(request, 'product_list.html', {'product_menu_list': product_menu_list})


class AddProductView(CreateView):
    model = Product
    template_name = 'add_product.html'
    fields = '__all__'


def ProductDetailView(request, pk):
    prod = Product.objects.all()
    newprod = prod[pk-1]
    return render(request, 'product_display.html', {'prod': newprod})


def accountHolderView(request):
    # print(customers)
    return render(request, 'accountHolders.html', {'accountHolders': customers})


def account(request, cus):
    if request.method == "POST":
        userName = request.POST.get('username')
        firstName = request.POST.get('firstname')
        quantity = request.POST.get('quantity')
        prodName = request.POST.get('product')

        Rec = Receipt(username=userName, first_name=firstName,
                      prod_name=prodName, prod_quantity=quantity, date=datetime.datetime.now().date())
        print("date right now is ", datetime.datetime.now().date())
        Rec.save()
    first_name = User.objects.filter(username=cus).values('first_name')
    last_name = User.objects.filter(username=cus).values('last_name')
    email = User.objects.filter(username=cus).values('email')
    username = User.objects.filter(username=cus).values('username')
    cust = {"first_name": first_name[0]['first_name'],
            'last_name': last_name[0]['last_name'], 'email': email[0]['email'], 'username': username[0]['username']}
    return render(request, 'account.html', {'customer': cust, 'Products': Product.objects.all()})


def historyView(request, mssg):
    Receipts = Receipt.objects.filter(username=mssg+" ")
    return render(request, 'history.html', {'Receipts': Receipts})
