
from django.urls import path
from .views import index, products

urlpatterns = [
    path('index/', index, name="index"),
    path('products/', products, name="products")

]
