from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Listing
def permission(view_func):
    def wrapper_func(request, *args, **kwargs):
        listing=Listing.objects.get(id)
        user=request.user
        if listing.lessor.user.id==user.id:
            return redirect('404')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func