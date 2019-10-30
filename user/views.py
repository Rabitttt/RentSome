from django.contrib.auth import authenticate,logout
from django.http import HttpResponseRedirect
from django.shortcuts import render , redirect,get_object_or_404,reverse
from .form import RegisterForm , LoginForm , UpdateForm
from .models import User
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse
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
        messages.success(request , "Başarıyla Giriş Yaptınız...")
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
        login(request,newUser)
        messages.success(request , "Başarıyla Hespa Oluşturdunuz...")
        return redirect("MainPage")
    context = {
        "form" : form
    }
    return render(request,"register.html",context)

def Logout(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız...")
    return redirect("MainPage")

def Detail(request,id):
    user = get_object_or_404(User,id=id)
    context = {
        "user" : user,
    }
    return render(request,"user_detail.html",context)

def Update(request,id):
    update = get_object_or_404(User,id = request.user.id)
    update_form = UpdateForm(request.POST or None, request.FILES or None ,instance=update)

    if update_form.is_valid():
        update = update_form.save()
        messages.success(request,"Profiliniz Başarıyla Güncellendi...")
        #return HttpResponseRedirect(reverse("user_detail", args=(request.user.id,)))
        return redirect("MainPage")

    return render(request,"profile_update.html",{"form":update_form,})


