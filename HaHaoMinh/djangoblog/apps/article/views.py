from __future__ import print_function
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .models import ArticleModel
from .forms import ArticleForm


def article_list(request):
    queryset = ArticleModel.objects.all().order_by("-timestamp")
    context = {
        "object_list": queryset,
        "name": "LIST ARTICLE"
    }
    return render(request, "article_list.html", context)


def article_create(request):
    if request.method == 'POST':

        form = ArticleForm(request.POST or None, request.FILES or None)
        print(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, "Create Article success!")
            return HttpResponseRedirect(instance.get_absolut_url())
        else:
            messages.error(request, "Create Article fail!")
    else:
        form = ArticleForm()

    context = {
        "form": form
    }

    return render(request, "article_form.html", context)


def article_detail(request, id=None):
    instance = get_object_or_404(ArticleModel, id=id)
    context = {
        "name": instance.name,
        "instance": instance
    }
    return render(request, "article_detail.html", context)


def article_update(request, id=None):
    instance = get_object_or_404(ArticleModel, id=id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=instance, )
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "<a href='#'>Item</a>Saved!", extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolut_url())

    context = {
        "name": instance.name,
        "instance": instance,
        "form": form
    }
    return render(request, "article_form.html", context)


def article_delete(request, id=None):
    instance = get_object_or_404(ArticleModel, id=id)
    instance.delete()
    messages.success(request, "Article deleted")
    return redirect("articles:article_list")
