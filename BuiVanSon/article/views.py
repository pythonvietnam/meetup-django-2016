from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

# Create your views here.
def article(request):
    list_article = Article.objects.all()
    return render(request, 'index.html', {'list_article': list_article})

