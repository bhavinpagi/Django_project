
from django.urls import path
from . import views

urlpatterns = [
    #path('index/', views.index, name="index"),
    path('products/', views.products, name="products"),
    path('user_reg/', views.user_reg, name="user_reg"),
    path('user_login/',views.user_login,name="user_login"),
    path('user_logout/', views.user_logout, name="user_logout"),
    path('update_product/<str:product_id>/', views.update_product, name="update_product"),
    path('add_product/', views.add_product, name="add_product"),

]
