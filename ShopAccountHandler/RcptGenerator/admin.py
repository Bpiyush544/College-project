from django.contrib import admin
from . models import (Product, Receipt, Amount)

# Register your models here.
# admin.site.register(Receipt)
# admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(Receipt)
admin.site.register(Amount)
