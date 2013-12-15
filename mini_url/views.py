# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from models import myURL
from forms import myURLForm


def list(request):
    """Display list of redirection"""
    urls = myURL.objects.order_by('-accessNb')
    return render(request, 'mini_url/list.html', locals())


def new(request):
    """Add a new redirection"""
    if request.method == "POST":
        form = myURLForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(list)
    else:
        form = myURLForm()

    return render(request, 'mini_url/new.html', {'form': form})



