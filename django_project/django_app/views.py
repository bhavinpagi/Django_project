from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Products


def index(request):
    print(request.method)
    return HttpResponse("<h1>Bhavin Pagi</h1>")

def products(request):
    products= Products.objects.all()
    print(products)
    return HttpResponse(products)
