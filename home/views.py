from http.client import HTTPResponse
from django.shortcuts import render
from house.choices import price_choices, bedroom_choices, state_choices
from house.models import Listing
# Create your views here.
def home(request):
    listings = Listing.objects.order_by('-list_date')[:6]
    context =  {
        'listings':listings,
       
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

def post(request):
    context={
    }
    return render(request,'home/post.html',context)
def listing(request):
    context={
    }
    return render(request,'listings/listing.html',context)
def testsearch(request):
    context={
    }
    return render(request,'listings/index.html',context)

def err404(request):
    context={
    }
    return render(request,'home/404.html',context)