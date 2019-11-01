from django.contrib import admin
from django.urls import path
from comment import views

app_name = "comment"

urlpatterns = [
    path("comments/<int:id>",views.ProductComment,name="comments"),
    path("nested_comment/<int:id>",views.NestedComment,name="nested_comment"),
]
