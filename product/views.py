from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render , get_object_or_404 , redirect
from django.contrib import messages
from .models import ProductModel
# Create your views here.
from user.models import User
from .form import RentForm ,DateForm


def List(request):
    product_list = ProductModel.objects.all()

    page = request.GET.get('page' , 1)

    paginator = Paginator(product_list ,6)

    try :
        products = paginator.page(page)
    except PageNotAnInteger :
        products = paginator.page(1)
    except EmptyPage :
        products = paginator.page(paginator.num_pages)

    for product in products :
        if product.hire_date == product.hire_end_date :
            product.is_available = False
            product.hire_end_date = None

    return render(request,"product_list.html",{"products" : products})


def detail(request,id):
    form = DateForm()
    product = ProductModel.objects.get(id = id)
    comment_list = product.product.all()
    context = {
        "product" : product ,
        "comment_list" : comment_list ,
        "form" : form,
    }
    return render(request , "product_detail.html" , context)

def my_products(request,id):
    user = get_object_or_404(User,id=id)
    hired = ProductModel.objects.filter(owner = user.id , is_available = False)
    wait_hire = ProductModel.objects.filter(owner = user.id , is_available = True)
    hired_from_me = ProductModel.objects.filter(hirer = user.id)
    context = {
        "hired" : hired,
        "wait_hire" : wait_hire,
        "hired_from_me" : hired_from_me,
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
    form = DateForm(request.POST or None)
    if form.is_valid():
        if request.user.money >= item.price:
            request.user.money -= item.price
            item.is_available = False
            item.hire_end_date = request.POST.get("hire_end_date")
            item.hirer = request.user
            item.save()
            return redirect("MainPage")
        messages.info(request,"Hesabınızda Yeterli Para Bulunmamaktadır...")
    return redirect("MainPage")
