from django.contrib.auth import authenticate
from django.shortcuts import render , redirect
from .form import RegisterForm , LoginForm
from .models import User
from django.contrib.auth import login
# Create your views here.


def MainPage(request):
    return render(request,"base.html")


def Login(request):
    form = LoginForm(request.POST or None)

    context = {
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)

        if user is None:
            return render(request,"login.html",context)

        login(request,user)
        return redirect("MainPage")

    return render(request,"login.html",context)

def Register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username = username)
        newUser.set_password(password)

        newUser.save()

        return redirect("MainPage")

    context = {
        "form" : form
    }

    return render(request,"register.html",context)
