from django.urls import path
from .views import login_users,index,register,logout_user

urlpatterns = [
    path("logout/", logout_user, name="logout"),
    path("register/", register, name="register"),
    path("login/", login_users, name="login"),
    path("", index, name="main"),
]
