from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from .models import Account


class InscriptionForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text="*",)
    username = forms.CharField(max_length=60, help_text="*",)

    class Meta:
        model = Account
        fields = [
            "email",
            "username",
            "password1",
            "password2",
            "phone",
            "date_of_birth",
        ]

    def clean_phone(self, *args, **kargs):
        phone = self.cleaned_data.get("phone")
        if len(phone) != 10:
            raise forms.ValidationError("Longueur du numéro incorrect")
        return phone


class AuthenticationForm(forms.ModelForm):

    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ("email", "password")

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data["email"]
            password = self.cleaned_data["password"]
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Email / Mot de passe incorrect")
