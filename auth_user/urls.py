from django.urls import path
from .views import login_users,index,register

urlpatterns = [
    path("login/", login_users, name="login"),
    path("register/", register, name="register"),
    path("", index, name="main"),
]
