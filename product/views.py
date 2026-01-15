from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.

def home(request):
    return render(request, 'home.html')
     

def offers_list(request):
    products = Product.objects.all()
    return render(request, 'products/offers.html', context={"products": products})

def offer_detail(request, product_id):
    product = Product.objects.filter(id=product_id).first()
    return render(request, "products/offer_detail.html", context={"product":product})
    


