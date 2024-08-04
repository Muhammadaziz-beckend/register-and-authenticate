import pprint
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate


def login_users(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("main")

    context = {"form": form}

    return render(request, "login.html", context)


def register(req):
    if req.user.is_authenticated:
        return redirect('main')
    form = RegisterForm()

    if req.method == "POST":
        form = RegisterForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req,user)
            return redirect("main")

    context = {
        "form": form,
    }
    return render(req, "register.html", context=context)


def logout_user(req):
    logout(req)
    return redirect('login')

@login_required(login_url="register")
def index(req):

    return render(req, "index.html")
