from django.shortcuts import render
from django.contrib.auth.models import User
from .form import RegisterForm
from django.http import HttpResponse
from .form import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

def register_view(request):
    if request.method == "GET":
        forms = RegisterForm()
        return render(request, 'users/register.html', context={"form": forms})
    elif request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.cleaned_data.__delitem__('confirm_password')
            User.objects.create_user(**form.cleaned_data)
            return HttpResponse(f"User {form.cleaned_data['username']} registered successfully")
        return HttpResponse("Invalid data, please try again.")

def login_view(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'users/login.html', context={"form": form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
         user = authenticate(**form.cleaned_data)
         if user is not None:
          login(request, user)
          return redirect('home')
         else:
              return render(request, "users/login.html", {
                    "form": form, 
                    "error": "Неверный логин или пароль"
                })
    else:
        form = LoginForm()
    return render(request, "users/login.htm", context={"form": form})

@login_required(login_url="/login/")
def logout_view(request):
    if request.method == "GET":
     logout(request)
     return redirect('home')

            
            