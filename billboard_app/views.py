# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
import datetime
from django import forms
from .forms import PostForm
from models import Post

# Create your views here.

def index(request):
    latest_post_list = Post.objects.order_by('-posts_pub_date')[:5]

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.pub_date = timezone.now()
            post.save()
                # return redirect('post_detail', pk=post.pk)
            return redirect('/')
    else:
        form = PostForm(initial= {'posts_pub_date':datetime.datetime.now()})

    context = {
        'latest_post_list': latest_post_list,
        'form': form
    }
    return render(request, 'billboard_app/index.html', context)


