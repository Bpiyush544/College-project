import datetime
from dis import dis
from math import prod
from django.shortcuts import render
from . models import Product, Receipt, Amount
# from django.views.generic import CreateView
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


def AddProductView(request):
    # CreateView
    # model = Product
    # template_name = 'add_product.html'
    # fields = '__all__'
    if request.method == "POST":
        prodname = request.POST.get('prodname')
        # we will try to precompute stuff here
        display_name = ""
        for c in prodname:
            if c != ' ':
                display_name += c
            else:
                display_name += '_'
        description = request.POST.get('description')
        image = request.POST.get('image')
        price = request.POST.get('price')
        prodAdd = Product(name=display_name, display_name=prodname, description=description,
                          image=image, price=price)
        prodAdd.save()
    return render(request, 'add_product.html')


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
        data = request.POST.get('data')
        newData = data.split(',')
        newData.pop()
        temp = 0
#       now with the help of data i can retrieve the product as well as quantity and save
        for item in newData:
            a = item.split('-')
            prodName = a[0]
            quantity = a[1]
            # print(type(quantity))
            temp += Product.objects.filter(
                name=prodName).values('price')[0]['price']*int(quantity)
            print(Product.objects.filter(
                name=prodName).values('price')[0]['price'])
            Rec = Receipt(username=userName, first_name=firstName, prod_name=prodName,
                          prod_quantity=quantity, date=datetime.datetime.now().date())
            Rec.save()
        t = Amount.objects.filter(username=cus).values('money')[0]['money']
        print(t)
        t += temp
        Amount.objects.filter(username=cus).update(money=t)
        t = Amount.objects.filter(username=cus).values('money')[0]['money']
        print(t)
    first_name = User.objects.filter(username=cus).values('first_name')
    last_name = User.objects.filter(username=cus).values('last_name')
    email = User.objects.filter(username=cus).values('email')
    username = User.objects.filter(username=cus).values('username')
    print("Here we are checking     ", (Amount.objects.filter(
        username=cus).values('username')))
    # print(username[0]['username'])
    if len(Amount.objects.filter(username=cus)) == 0:
        amnt = Amount(username=username[0]['username'],
                      first_name=first_name[0]['first_name'], money=0)
        amnt.save()
        # amnt = {"username": username[0]['username'],
        #         "first_name": first_name[0]['first_name'], "money": 0}
        # print(amnt)
    cust = {"first_name": first_name[0]['first_name'],
            'last_name': last_name[0]['last_name'], 'email': email[0]['email'], 'username': username[0]['username']}
    return render(request, 'account.html', {'customer': cust, 'Products': Product.objects.all(), 'amount': Amount.objects.filter(username=cus).values('money')[0]['money']})


def historyView(request, mssg):
    Receipts = Receipt.objects.filter(username=mssg+" ")
    letsGo = {}
    for rec in Receipts:
        if rec.date.strftime("%Y/%m/%d") in letsGo:
            letsGo[rec.date.strftime("%Y/%m/%d")].append(rec)
        else:
            letsGo[rec.date.strftime("%Y/%m/%d")] = []
            letsGo[rec.date.strftime("%Y/%m/%d")].append(rec)
    print(letsGo)
    return render(request, 'history.html', {'letsGo': letsGo})


#  we can update the initial model of Product and include another field into it that would be display name field
#  we could recompute the initial name we gave to the product to a name which include underscores
