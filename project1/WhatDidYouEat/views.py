from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Content
from .forms import ContentForm
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    posts=Content.objects.all
    return render(request, 'WhatDidYouEat/home.html', {'post_list': posts})

def today(request):
    if request.method=='POST':
        form =ContentForm(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.published_date=timezone.now()
            post.save()
            return redirect('home')
    else:
        form=ContentForm()
    return render(request, 'WhatDidYouEat/today.html', {'form':form})

def detail(request, pk):
    post=get_object_or_404(Content, pk=pk)
    return render(request, 'WhatDidYouEat/detail.html', {'post':post})

def edit(request, pk):
    post=get_object_or_404(Content, pk=pk)
    if request.method=="POST":
        form=ContentForm(request.POST, instance=post)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.published_date=timezone.now
            post.save()
            return redirect('detail', pk=post.pk)
    else:
        form=ContentForm(instance=post)
    return render(request, 'WhatDidYouEat/edit.html', {'form':form})

def delete(request, pk):
    post=get_object_or_404(Content, pk=pk)
    post.delete()
    return redirect('home')