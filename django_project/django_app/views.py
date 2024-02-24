from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Products
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

def index(request):
    print(request.method)
    return HttpResponse("<h1>Bhavin Pagi</h1>")

def products(request):
    products= Products.objects.all()
    return render(request,'product.html', context={'products':products})

@csrf_exempt
def user_reg(request):
    # print(request.GET.get('abc'))
    # print(request.GET.get('lmn'))
    message = ""
    if request.method == "POST":
        print("inside post method")
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        existing_user = User.objects.filter(username=username).first()
        print(existing_user, "existing_user")
        if existing_user:
            message = "This username is already taken! Use another one."
        elif password != confirm_password:
            message = "Password doesnt match"
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            
    context = {"message": message}
    return render(request=request, template_name='user_reg.html', context=context)