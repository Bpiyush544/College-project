from email import message
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField
# Create your models here.

# Product Updation is also left so we need to write that as well


class Product(models.Model):
    prod_id = models.AutoField
    name = models.CharField(max_length=255, default="")
    display_name = models.CharField(
        max_length=255, null=True, blank=True, default="")
    price = models.IntegerField()
    description = models.CharField(max_length=2000, null=True, blank=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(
        null=True, blank=True, upload_to="images/new")

    def __str__(self):
        return self.display_name

    def get_absolute_url(self):
        return reverse('home')


# class Profile(models.Model):
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     bio = models.TextField()
#     profile_pic = models.ImageField(
#         null=True, blank=True, upload_to="images/profile/")
#     website_url = models.CharField(max_length=255, null=True, blank=True)
#     facebook_url = models.CharField(max_length=255, null=True, blank=True)

#     def __str__(self):
#         return str(self.user)

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


class Contact(models.Model):
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    email = models.CharField(max_length=1023)
    message = models.CharField(max_length=5000)
    date = models.DateField()

    def __str__(self):
        return self.username
