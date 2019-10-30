from django.contrib import admin
from django.urls import path
from user import views

app_name = "user"


urlpatterns = [
    path('login/',views.Login, name = 'login'),
    path('register/',views.Register, name = 'register'),
    path('logout/',views.Logout,name = "logout"),
    path('detail/<int:id>/',views.Detail,name="user_detail"),
    path('update/<int:id>/',views.Update,name="update"),
]
