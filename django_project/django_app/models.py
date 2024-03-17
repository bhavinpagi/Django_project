import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Products(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    price = models.FloatField(default=10)
    product_image = models.ImageField()
    active = models.BooleanField(default=True)
    rating = models.FloatField()
    available_quentity = models.IntegerField()
    pending_quentity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return f"Name : {self.product_name}, Discription: {self.product_description}, Rating: {self.rating}, Price: {self.price}"
    # def __int__(self):
    #     return f"Rating: {self.rating}"

"""
For one to many scnearios we can create a new intermediatery table as "User_CartModel" which 
will accept only user_id and product_id for mapping of UserCart   
Not going to follow this approach, but doable
""" 

class UserCartModel(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        verbose_name_plural = "User Carts"

class UserAddress(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    line1 = models.CharField(max_length=100)
    line2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.BigIntegerField()
    country = models.CharField(max_length=100)

PAYMENT_CHOICES = (
    ("CASH_ON_DELIVERY", "CASH_ON_DELIVERY"),
    ("UPI", "UPI"),
    ("NET_BANKING", "NET_BANKING")
)
class UserOrders(models.Model):
    order_id = models.CharField(max_length=50)
    address_id = models.ForeignKey(UserAddress, on_delete=models.CASCADE)
    order_placed_at = models.DateTimeField(auto_now_add=True)
    product_total_quantity = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    product_image = models.ImageField()
    product_quantity = models.IntegerField()
    payment_type = models.CharField(max_length=20, choices = PAYMENT_CHOICES, default = 'CASH_ON_DELIVERY')
    total_amount = models.FloatField() 

    class Meta:
        verbose_name_plural = "User Orders"

