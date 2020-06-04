from django.shortcuts import render, redirect

from .forms import AuthenticationForm, InscriptionForm


def inscription_view(request):
    form = InscriptionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(authentication_view)

    return render(request, "user/inscription.html", {"form": form})


def authentication_view(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request.Form)
        if form.is_valid():
            return redirect(home)
        else:
            print(form.errors)

    return render(request, "user/authentication.html", {"form": form})
