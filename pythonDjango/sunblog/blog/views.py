from django.shortcuts import render
from django.http import HttpResponse
from blog.models import *
from datetime import date

# Create your views here.

def hello(request):
    name='sun'
    age=18
    # return HttpResponse('<h1>hello world:%$</h1>'%offset)
    return render(request,'hello.html',locals())

def index(request):
    d=date.today()
    articles=Article.objects.all()
    return render(request,'index.html',locals())

def article(request,pid):
    articles=Article.objects.get(id=pid)
    return render(request,'article.html',locals())
