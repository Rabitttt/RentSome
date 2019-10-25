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
    form = RentForm(request.POST or None)
    context = {
        "form" : form,
    }
    if form.is_valid():
        name = form.cleaned_data.get("name")
        price = form.cleaned_data.get("price")

        item = ProductModel(name = name ,price = price,owner = request.user)

        item.save()

        messages.success(request,"Ürün Başarıyla Eklendi...")
        return redirect("MainPage")
    return render(request,"rent_item.html",context)


