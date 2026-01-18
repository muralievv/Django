from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .form import ProductForm

# Create your views here.

def home(request):
    if request.method == "GET":
     return render(request, 'home.html')
     

def offers_list(request):
    if request.method == "GET":
     products = Product.objects.all()
     return render(request, 'products/offers.html', context={"products": products})

def offer_detail(request, product_id):
    if request.method == "GET":
     product = Product.objects.filter(id=product_id).first()
     return render(request, "products/offer_detail.html", context={"product":product})


def offer_create(request):
    if request.method == "GET":
        form = ProductForm()
        return render(request, 'products/offer_create.html', context={"form": form})
    elif request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            Product.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                salary=form.cleaned_data['salary'],
                photo=form.cleaned_data['photo']
            )
        return HttpResponse(f"Offer {form.cleaned_data['title']} created successfully")

    


