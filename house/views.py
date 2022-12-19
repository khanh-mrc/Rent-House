from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.urls import reverse
from django.http import HttpResponseRedirect
from house.choices import price_choices, bedroom_choices, city_choices, area_choices
from .models import Listing
from .forms import ListingForm
from accounts.models import Profile
from contacts.models import Contact
from accounts.forms import *

@login_required(login_url='login' )


@login_required(login_url='login' )
def listing_dashboard(request):
    listings=Listing.objects.filter(lessor=request.user.Profile).order_by('-list_date')
    user_contacts = Contact.objects.filter(user_id = request.user.id).order_by('-contact_date')
    lessor_contacts = Contact.objects.filter(lessor_id = request.user.id).order_by('-contact_date')
    paginator = Paginator(listings,11)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context={
        'listings':paged_listings,
        'contacts': user_contacts,
        'contactsrc': lessor_contacts,
    }
    return render(request, "accounts/dashboard.html",context)

@login_required(login_url='login' )
def listing_delete(request, pk):
    listing=Listing.objects.get(id=pk)
    if request.method== "POST":
        listing.delete()
        return redirect('/')
    context={
        'item': listing
    }
    return render(request, 'listings/listing_delete.html',context)

@login_required(login_url='login' )
def listing_update(request, pk):
    listing=Listing.objects.get(id=pk)
    form=ListingForm(instance=listing)
    if request.method== "POST":
        form = ListingForm(request.POST,request.FILES, instance= listing)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={
        'form': form
    }
    return render(request, 'listings/listing_create.html',context)

@login_required(login_url='login' )
def listing_create(request):
    form = ListingForm()
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.lessor = request.user.Profile
            instance.save()
            return redirect('/listings')

    Profile = request.user.Profile
    form1 = ProfileForm(instance=Profile)
    if request.method == "POST":
        form1 = ProfileForm(request.POST, request.FILES,instance=Profile)
        if form1.is_valid():
            form1.save()
            #return redirect('/listings')
    context = {
        'form':form,
        'form1':form1
    }
    context={
        "form": form
    }
    return render(request,"listings/listing_create.html",context)

def listing_list(request):
    listings=Listing.objects.order_by('-list_date')
    paginator = Paginator(listings,6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context={
        'listings':paged_listings,
        'listings':listings,
        "city_choices": city_choices,
        "price_choices":price_choices,
        "area_choices":area_choices,
        "bedroom_choices":bedroom_choices,
    }
    return render(request, "listings/listings.html",context)

def listing_retrieve(request,listing_id):
    listing= Listing.objects.get(pk=listing_id)

    fav = bool

    if listing.favourites.filter(id=request.user.id).exists():
        fav = True

    listings2=Listing.objects.order_by('-list_date')[:6]
    context={
        "listing":listing,
        "listings2": listings2,
        'fav': fav
    }
    return render(request, "listings/detail.html",context)

def search(request):
    queryset_list = Listing.objects.order_by('price','area','-list_date')
    
    # Keywords 
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(address__icontains=keywords) |  queryset_list.filter(description__icontains=keywords) | queryset_list.filter(title__icontains=keywords)
    
    # city 
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact = city)

    # area 
    if 'area' in request.GET:
        area = request.GET['area']
        if area:
            queryset_list = queryset_list.filter(area__lte = area)
    
    # price 
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte= price)
    #Page
    paginator = Paginator(queryset_list,6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
 
    context =  {
        
        "city_choices": city_choices,
        "price_choices":price_choices,
        "area_choices":area_choices,
        "bedroom_choices":bedroom_choices,
        "listings":paged_listings,
        "values":request.GET,
    }
    return render(request,'listings/search.html',context)


