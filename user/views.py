from django.contrib.auth import authenticate,logout
from django.shortcuts import render , redirect
from .form import RegisterForm , LoginForm
from .models import User
from django.contrib.auth import login
from django.contrib import messages
# Create your views here.
from rentsome import urls



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
            messages.info(request , "Kullanıcı Adı Veya Parola Hatalı...")
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
        messages.success(request,"Başarıyla Giriş Yaptınız...")
        return redirect("MainPage")
    context = {
        "form" : form
    }

    return render(request,"register.html",context)

def Logout(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız...")
    return redirect("login")