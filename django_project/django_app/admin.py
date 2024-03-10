from django.contrib import admin
from django_app.models import Products, UserCartModel, UserOrders, UserAddress


# Register your models here.
admin.site.register(Products)
admin.site.register(UserCartModel)
admin.site.register(UserOrders)
admin.site.register(UserAddress)
