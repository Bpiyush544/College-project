from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
# Create your models here.


class Product(models.Model):
    prod_id = models.AutoField
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.CharField(max_length=2000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True,
                              upload_to="images/product/")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(
        null=True, blank=True, upload_to="images/profile/")
    website_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

# class Profile(models.Model):
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     bio = models.TextField()
#     profile_pic = models.ImageField(
#         null=True, blank=True, upload_to="images/profile/")
#     website_url = models.CharField(max_length=255, null=True, blank=True)
#     facebook_url = models.CharField(max_length=255, null=True, blank=True)

#     def __str__(self):
#         return str(self.user)


# class Receipt(models.Model):
    # username = models.CharField(max_length=255, default="")
    # first_name = models.CharField(max_length=255, default="")
    # prod_name = models.CharField(max_length=255, default="")
    # prod_quantity = models.IntegerField()
    # date = models.DateTimeField()
    # email = models.CharField(max_length=255, default="")
    # mobile_number = models.IntegerField()
    # image = models.ImageField(null=True, blank=True, upload_to='images/')

class Receipt(models.Model):
    username = models.CharField(max_length=255, default="")
    first_name = models.CharField(max_length=255, default="")
    prod_name = models.CharField(max_length=255, default="")
    prod_quantity = models.IntegerField()

    date = models.DateField()

    def __str__(self):
        return self.prod_name


class Amount(models.Model):
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    money = models.IntegerField()

    def __str__(self):
        return self.username
