from django.shortcuts import render , get_object_or_404 , redirect,reverse
from django.contrib import messages
# Create your views here.
from .models import Comment
from .form import CommentForm
from product.models import ProductModel
from django.contrib.auth.decorators import login_required

@login_required(login_url = "user:login")
def ProductComment(request,id):
    product = get_object_or_404(ProductModel,id=id)
    newComment = Comment(sender = request.user , reciever = product)
    newComment.comment = request.POST.get("comment")
    newComment.save()
    return redirect(reverse("product:detail",kwargs={"id":id}))

@login_required(login_url = "user:login")
def NestedComment(request,id):
    pass
