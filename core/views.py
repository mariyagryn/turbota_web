from django.shortcuts import render
from .models import News


def index(request):
    news_list = News.objects.all()
    return render(request, 'core/index.html', {'news_list': news_list})
