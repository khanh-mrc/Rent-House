from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from house.choices import price_choices, bedroom_choices, state_choices

from .models import Listing

def hello(request):
   context={}
   return render(request,"listings/hello.html",context)

def listing_list(request):
    listings=Listing.objects.all()
    context={
        "listings": listings
    }
    return render(request, "listings/testlist0.html",context)

def listing_retrieve(request,listing_id):
    listing= Listing.objects.get(pk=listing_id)
    context={
        "listing":listing
    }
    return render(request, "listings/detail.html",context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # Keywords 
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains = keywords)
    
    # city 
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact = city)
    
    # state 
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact = state)

    # bedrooms 
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte = bedrooms)
    
    # price 
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte = price)


    context =  {
        "price_choices":price_choices,
        "state_choices":state_choices,
        "bedroom_choices":bedroom_choices,
        "listings":queryset_list,
        "values":request.GET,
    }
    return render(request,'listings/search.html',context)

# Create your views here.
