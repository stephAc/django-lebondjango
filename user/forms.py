from django import forms

from .models import User


class AuthenticationForm(forms.Form):
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=50, required=True)


class InscriptionForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "name", "password", "age", "number"]

    def clean_number(self, *args, **kargs):
        number = self.cleaned_data.get("number")
        if len(number) < 10 or len(number):
            raise forms.ValidationError("Longueur du numéro incorrect")
        return number
