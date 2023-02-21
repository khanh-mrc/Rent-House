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
                            #sender
                            user_id =user_id,
                            name = name,
                            email = email,
                            phone = phone,
                            message = message,
                            #recieved
                            lessor_id =lessor_id,
                            lessor_name=lessor_name,
                            lessor_phone=lessor_phone,
                            )

        # Check if request has already been made.
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id = listing_id,user_id = user_id)
            if has_contacted:
                messages.error(request,": You have aleady made a request before")
                return redirect('/listings/'+ listing_id)
        contact.save()
        # Send mail
        print(lessor_email)
        send_mail(
            "You have a rental request from Rental Home",
            'There has been a request for your Property: '+ listing  + 
            '\nInfo: '+ 
            '\n   Name: ' + name +
            '\n   Email: ' + email+
            '\n   Phone Number: '+phone +
            '\n   Messages: ' +message+
            "\n. Sign in to your account management for more info.",
            "Rental Home <rentalhouses15@gmail.com>",
            [lessor_email],
            fail_silently=False)
    
        messages.success(request,"Your request has been submitted. We have notified to the Lessor. "+
        "The lessor will contact you soon.")
        
        return redirect('/listings/'+listing_id)