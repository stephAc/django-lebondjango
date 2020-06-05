from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from .forms import InscriptionForm, AuthenticationForm


def inscription_view(request):
    print("inscription_view")
    context = {}
    if request.POST:
        form = InscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            context["registration_form"] = form
    else:
        form = InscriptionForm()
        context["registration_form"] = form

    return render(request, "user/inscription.html", context)


def login_view(request):
    print("login_view")
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("home")
    if request.POST:
        print("post")
        form = AuthenticationForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            print("valid")
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(email=email, password=password)
            print(user)
            if user:
                login(request, user)
                return redirect("home")
    else:
        form = AuthenticationForm()

    context["login_form"] = form
    return render(request, "user/login.html", context)


def logout_view(request):
    logout(request)
    return redirect("home")
