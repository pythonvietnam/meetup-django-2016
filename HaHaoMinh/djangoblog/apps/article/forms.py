from django import forms

from .models import ArticleModel


class ArticleForm(forms.ModelForm):
    class Meta:
        model = ArticleModel
        fields = {
            "name",
            "image",
            "content",
            "category",
        }
