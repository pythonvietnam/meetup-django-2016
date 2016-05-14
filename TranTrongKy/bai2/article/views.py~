from django.shortcuts import render
from article.models import article

def home(request):
	list_article = article.objects.all()
	return render(request,"index.html",{"list_article":list_article})

