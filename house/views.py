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
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from .decorators import *
@login_required(login_url='login' )


@login_required(login_url='login' )
def listing_dashboard(request):
    listings=Listing.objects.filter(lessor=request.user.Profile).order_by('-id')
    user_contacts = Contact.objects.filter(user_id = request.user.id).order_by('-contact_date')
    lessor_contacts = Contact.objects.filter(lessor_id = request.user.id).order_by('-contact_date')
    paginator = Paginator(listings,12)
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
    user=request.user
    if request.method== "POST":
        if listing.lessor.user.id==user.id:
            print("Co Quyen")
            listing.delete()
            return redirect('/')
        else:
            print("Khong Co Quyen")
            return redirect('404')
    context={
        'item': listing
    }
    return render(request, 'listings/listing_delete.html',context)

@login_required
def listing_update(request, pk):
    listing=Listing.objects.get(id=pk)
    form=ListingForm(instance=listing)
    if request.method== "POST":
        form = ListingForm(request.POST,request.FILES, instance= listing)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')
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
            messages.success(request,"Your Post has been created successfully !")
            return redirect('/dashboard')

    Profile = request.user.Profile
    form1 = ProfileForm(instance=Profile)

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
        "city_choices": city_choices,
        "price_choices":price_choices,
        "area_choices":area_choices,
        "bedroom_choices":bedroom_choices,
    }
    return render(request, "listings/listings.html",context)

def listing_retrieve(request,listing_id):
    listing= Listing.objects.get(pk=listing_id)

    fav = bool
    ex_id = listing.pk

    if listing.favourites.filter(id=request.user.id).exists():
        fav = True

    listings2=Listing.objects.order_by('-list_date')[:6]
    other_result=Listing.objects.all()
    other_result=Listing.objects.filter(~Q(id = ex_id))
    other_result=other_result.filter(address__unaccent__icontains=listing.address) |  other_result.filter(description__unaccent__icontains=listing.description) | other_result.filter(title__unaccent__icontains=listing.title) | other_result.filter(city__unaccent__icontains=listing.city).order_by('price','area','-list_date')[:6]
    context={
        "listing":listing,
        "listings2": listings2,
        "other_result": other_result,
        'fav': fav
    }
    return render(request, "listings/detail.html",context)

def search(request):
    queryset_list = Listing.objects.order_by('price','area','-list_date')
    
    # Keywords 
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(address__unaccent__icontains=keywords) |  queryset_list.filter(description__unaccent__icontains=keywords) | queryset_list.filter(title__unaccent__icontains=keywords) | queryset_list.filter(city__unaccent__icontains=keywords)
    
    # city 
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact = city)
    
     # price 
    if 'price' in request.GET:
        price = request.GET['price']
        print(price)
        if price:
            if price == '10000000':
                print(price)
                queryset_list = queryset_list.filter(price__gte = price)
                print("tren 10 tr")
            else:
                queryset_list = queryset_list.filter(price__lte = price)
                print("duoi 10 tr")
            
    # area
    if 'area' in request.GET:
        area = request.GET['area']
        print(area)
        if area:
            if area == '90':
                print(area)
                queryset_list = queryset_list.filter(area__gte = area)
                print("tren 90 m2")
            else:
                    queryset_list = queryset_list.filter(area__lte = area)

     
              


    #Page
    paginator = Paginator(queryset_list,20)
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


