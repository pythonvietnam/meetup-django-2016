from django import forms

from .models import SignUpModel


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUpModel
        fields = {
            "first_name",
            "last_name",
            "email",
            "password",
            "password2",
        }
