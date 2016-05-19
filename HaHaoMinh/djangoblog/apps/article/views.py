from __future__ import print_function
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from urllib import quote_plus
from django.utils import timezone

from .models import ArticleModel
from .forms import ArticleForm


def article_list(request):
    queryset_list = ArticleModel.objects.all().order_by("-timestamp")
    paginator = Paginator(queryset_list, 15)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
        "name": "LIST ARTICLE"
    }
    return render(request, "article_list.html", context)


def article_create(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Create Article success!")
        return HttpResponseRedirect(instance.get_absolut_url())
    else:
        messages.error(request, "Create Article fail!")

    context = {
        "form": form,
        "action": "Create"
    }

    return render(request, "article_form.html", context)


def article_detail(request, id=None):
    instance = get_object_or_404(ArticleModel, id=id)
    share_string = quote_plus(instance.content)
    context = {
        "name": instance.name,
        "instance": instance,
        "share_string": share_string
    }
    return render(request, "article_detail.html", context)


def article_update(request, id=None):
    instance = get_object_or_404(ArticleModel, id=id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "<a href='#'>Item</a>Saved!", extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolut_url())

    context = {
        "name": instance.name,
        "instance": instance,
        "form": form,
        "action": "Save"
    }
    return render(request, "article_form.html", context)


def article_delete(request, id=None):
    instance = get_object_or_404(ArticleModel, id=id)
    instance.delete()
    messages.success(request, "Article deleted")
    return redirect("articles:article_list")
