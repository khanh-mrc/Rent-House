from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator
from house.choices import price_choices, bedroom_choices, state_choices
from .models import Listing
from .forms import ListingForm

def listing_create(request):
    form = ListingForm()
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/listings')
    context={
        "form": form
    }
    return render(request,"listings/listing_create.html",context)

def listing_list(request):
    listings=Listing.objects.all()
    context={
        "listings": listings
    }
    return render(request, "listings/listings.html",context)
'''
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published = True)
    paginator = Paginator(listings,3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings':paged_listings}
         
    return render(request,'listings/listings.html',context)
'''
def listing_retrieve(request,listing_id):
    listing= Listing.objects.get(pk=listing_id)
    listings2=Listing.objects.order_by('-list_date')[:6]
    context={
        "listing":listing,
        "listings2": listings2
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
