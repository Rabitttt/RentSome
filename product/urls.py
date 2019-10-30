from django.contrib import admin
from django.urls import path
from product import views

app_name = "product"

urlpatterns = [
    path("detail/<int:id>",views.detail,name = 'detail'),
    path("myproducts/<int:id>",views.my_products,name='myproducts'),
    path("rent_item/",views.rent_items,name='rent_item'),
    path("rent/<int:id>",views.rental,name='rent'),
]
