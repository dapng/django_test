from django import forms
from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm

# Create your views here.

def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})


def create(request):
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма не верна'

    form = ArticlesForm()

    data = {
        'form': form,
        # 'error': error,
    }
    return render(request, 'news/news_create.html', data)