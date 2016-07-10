from django import forms

from .models import Career
from captcha.fields import CaptchaField


class CareerForm(forms.ModelForm):
  captcha = CaptchaField()

  class Meta:
    model = Career
    exclude = [
      "timestamp"
    ]
