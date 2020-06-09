from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .forms import InscriptionForm, AuthenticationForm, UserUpdateForm
from articles.models import Articles


def inscription_view(request):
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
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("articles:index")
    if request.POST:
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect("articles:index")
    else:
        form = AuthenticationForm()

    context["login_form"] = form
    return render(request, "user/login.html", context)


def logout_view(request):
    logout(request)
    return redirect("articles:index")


@login_required(login_url="/user/login")
def my_ad_view(request):
    user = request.user
    articles = Articles.objects.filter(owner=user)
    return render(request, "user/ad.html", {"ads": articles})


@login_required(login_url="/user/login")
def profil_view(request):
    return render(request, "user/profil.html", {})


@login_required(login_url="/user/login")
def update_profil(request):

    if request.POST:
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profil")
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, "user/update_profil.html", {"form": form})
