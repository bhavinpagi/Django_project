import datetime

from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Products, UserCartModel
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


def index(request):
    print(request.method)
    return HttpResponse("<h1>Bhavin Pagi</h1>")


# def products(request):
#     products=Products.objects.all()
#     print(products)
#     return HttpResponse(products)

def products(request):
    products= Products.objects.all().order_by('-updated_at')
    return render(request,'product.html', context={'products':products})

@csrf_exempt
def user_reg(request):
    # print(request.GET.get('abc')) 
    # print(request.GET.get('lmn'))
    message1 = ""
    message2 = ""
    if request.method == "POST":
        print("inside post method")
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        existing_user = User.objects.filter(username=username).first()
        print(existing_user, "existing_user")
        if existing_user:
            message1 = "This username is already taken! Use another one."
        elif password != confirm_password:
            message2 = "Password doesnt match"
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            
    context = {"message1": message1, "message2":message2}
    return render(request=request, template_name='user_reg.html', context=context)

def user_login(request):
    message = ""
    if request.method == "POST":
        csrf_token = request.POST.get('csrfmiddlewaretoken')
        email = request.POST.get('email')
        password = request.POST.get('password')

        username = User.objects.filter(email=email).first()
        print(username, type(username))
        is_authenticated = authenticate(request, username=username, password=password)
        # if not username:
        #     message = "Your email is not registered with us"
        if not is_authenticated:
            message = "Password or email doesnt matches. Email maybe not registered with us"
        elif username:            
            login(request, user=username)
            print(username.username, type(username.username), "username.username")
            return redirect('products')
    context = {"message": message}
    return render(request=request, template_name='user_login.html', context=context)


def user_logout(request):
    logout(request)
    return redirect('products')



def update_product(request, product_id):
    product_object = Products.objects.filter(id=product_id).first()
    if not product_object:
        return redirect('products')
    
    if request.method == "POST":
        product_name = request.POST.get('product_name')
        product_description = request.POST.get('product_description')
        product_price = request.POST.get('product_price')
        product_rating = request.POST.get('product_rating')
        product_quantity = request.POST.get('product_quantity')
        print(product_name, product_description, product_price, product_rating, product_quantity)

        product_obj = Products.objects.filter(id=product_id).first()
        product_obj.product_name = product_name
        product_obj.product_description = product_description      
        product_obj.price = product_price      
        product_obj.product_rating = product_rating      
        product_obj.available_quentity = product_quantity      
        product_obj.updated_at = datetime.datetime.now()
        product_obj.save()
        return redirect("products")
    context = {"product_object": product_object}
    return render(request=request, template_name='update_product.html', context=context)

def add_product(request):
    print(request.user.is_authenticated)
    if not request.user.is_authenticated:
        return redirect('user_login')
    
    if request.method == "POST":
        product_name = request.POST.get('product_name')
        product_description = request.POST.get('product_description')
        product_price = request.POST.get('product_price')
        product_rating = request.POST.get('product_rating')
        available_quantity = request.POST.get('available_quantity')
        product_image = request.FILES.get('product_image')
        
        product_obj = Products.objects.create(
            product_name=product_name,
            product_description=product_description,
            price=product_price,
            rating=product_rating,
            pending_quentity=0,
            available_quentity=available_quantity,
            product_image=product_image
        )
        product_obj.save()
        return redirect('products')
    context = {}
    return render(request, 'add_product.html', context)

def delete_product(request, product_id):
    Products.objects.filter(id=product_id).delete()
    return redirect('products')

def add_to_cart(request, product_id):
    product_obj = Products.objects.filter(id=product_id).first()
    user_obj = User.objects.filter(username=request.user.username).first()

    if request.method == "POST":
        cart_value = request.POST.get('cart_value')
        already_added_obj = UserCartModel.objects.filter(product_id=product_id).first()
        if already_added_obj:
            already_added_obj.quantity += int(cart_value)
            already_added_obj.save()
        else:
            cart_obj = UserCartModel.objects.create(
                product_id = product_obj,
                user_id = user_obj,
                quantity = cart_value
            )
            cart_obj.save()
        print(cart_value, "cart_value")
    return redirect('display_cart')

def display_cart(request):
    user_obj = User.objects.filter(username=request.user.username).first()
    cart_obj = UserCartModel.objects.filter(user_id_id=user_obj.id)
    context = {"user_obj": user_obj, "cart_obj": cart_obj}
    return render(request, 'display_cart.html', context)

