
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('products/', views.products, name="products"),
    path('user_reg/', views.user_reg, name="user_reg"),
]
