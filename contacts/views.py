from django.shortcuts import render, redirect
from .models import Contact
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
def contact(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        lessor_id = request.POST['lessor_id']
        lessor_name = request.POST['lessor_name']
        lessor_phone = request.POST['lessor_phone']
        lessor_email = request.POST['lessor_email']

        contact = Contact(listing_id = listing_id,
                            listing = listing,
                            name = name,
                            email = email,
                            phone = phone,
                            message = message,
                            user_id =user_id,
                            lessor_id =lessor_id,
                            lessor_name=lessor_name,
                            lessor_phone=lessor_phone,
                            )

        # Check if inquiry has already been made.
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id = listing_id,user_id = user_id)
            if has_contacted:
                messages.error(request,"You have aleady made an inquiry")
                return redirect('/listings/'+ listing_id)
        contact.save()
        # Send mail
        '''
        send_mail(
            "Property Listing Inquiry",
            'There has been an inquiry for listing '+ listing + 
            ". Sign in to the admin panel for more info."+message,
            'khanhpham.2004.02@gmail.com',
            [contact.email,],
            fail_silently=False)
    
        messages.success(request,"Your request has been submitted. "+
        "We will get backto you soon.")
        '''
        return redirect('/listings/'+listing_id)