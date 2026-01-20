from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .form import ProductForm
from django.contrib.auth.decorators import login_required
from .form import SearchForm
from django.db.models import Q

# Create your views here.
# GET - для просмтора данных
# POST - для создания/изменения данных
# PUT - для обновления данных
# PATCH - для частичного обновления данных
# DELETE - для удаления данных

# lt products.salary < 100
# gt products.salary > 100
# lte products.salary <= 100
# gte products.salary >= 100

def home(request):
    if request.method == "GET":
     return render(request, 'home.html')


@login_required(login_url="/login/")
def offers_list(request):
    products = Product.objects.all()
    if request.method == "GET":
        forms = SearchForm()
        search = request.GET.get("search")
        category = request.GET.get("category")
        salary = request.GET.get("salary")
        tags = request.GET.getlist("tags")
        if category:
            products = products.filter(category=category)
        if search:
            products = products.filter(Q(title__icontains=search) | Q(description__icontains=search))
        if salary:
            if salary == "1":
                products = products.filter(salary__lte=100)
            elif salary == "2":
                products = products.filter(salary__gt=100)
        if tags:
            products = products.filter(tag__in=tags)
        return render(request, 'products/offers.html', context={"products": products, "form": forms})
     

@login_required(login_url="/login/")
def offer_detail(request, product_id):
    if request.method == "GET":
     product = Product.objects.filter(id=product_id).first()
     return render(request, "products/offer_detail.html", context={"product":product})


@login_required(login_url="/login/")
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

    


