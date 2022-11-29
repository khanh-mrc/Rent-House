from http.client import HTTPResponse
from django.shortcuts import render
# Create your views here.
def home(request):
    context={
    }
    return render(request,'home/index.html',context)

def about(request):
    context={
    }
    return render(request,'home/about.html',context)

def detail(request):
    context={
    }
    return render(request,'home/detail.html',context)

def search(request):
    context={
    }
    return render(request,'home/search.html',context)

def test(request):
    context={
    }
    return render(request,'home/test.html',context)