from django.shortcuts import render , get_object_or_404 , redirect
from django.contrib import messages
from .models import ProductModel
# Create your views here.
from user.models import User
from .form import RentForm


def List(request):
    product = ProductModel.objects.all()
    return render(request,"product_list.html",{"product":product})

def detail(request,id):
    product = ProductModel.objects.filter(id = id)
    context = {
        "product" : product,
    }
    return render(request,"product_detail.html",context)

def my_products(request,id):
    user = get_object_or_404(User,id=id)
    product = ProductModel.objects.filter(owner = user.id)
    context = {
        "product" : product,
    }
    return render(request,"my_product.html",context)

def rent_items(request):
    form = RentForm(request.POST or None,request.FILES or None)
    context = {
        "form" : form,
    }
    if form.is_valid():
        item = form.save(commit = False)

        item.owner = request.user

        item.save()

        messages.success(request,"Ürün Başarıyla Eklendi...")
        return redirect("MainPage")
    return render(request,"rent_item.html",context)


def rental(request,id):
    item = ProductModel.objects.get(id = id)
    if request.user.money >= item.price:
        request.user.money -= item.price
        item.is_available = False
        item.hirer = request.user
        item.save()
        return redirect("MainPage")
    messages.info(request,"Hesabınızda Yeterli Para Bulunmamaktadır...")
    return redirect("MainPage")