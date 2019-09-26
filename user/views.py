from django.shortcuts import render , redirect
from .form import RegisterForm
from .models import User
# Create your views here.


def MainPage(request):
    return render(request,"base.html")


def Login(request):


    return render(request,"login.html")

def Register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("usernmae")
        password = form.cleaned_data.get("password")

        newUser = User(username = username)
        newUser.set_password(password)

        newUser.save()

        return redirect("MainPage")

    context = {
        "form" : form
    }

    return render(request,"register.html",context)
