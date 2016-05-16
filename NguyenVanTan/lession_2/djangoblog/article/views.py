from django.shortcuts import render
from article.models import Article
# Create your views here.

def home(request):
	list_article = Article.objects.all()
	return render(request, "index.html",{"list_article":list_article})
