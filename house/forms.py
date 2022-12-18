from django.forms import ModelForm
from .models import Listing
from accounts.models import Profile
from django.forms.models import inlineformset_factory
from django import forms
class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields =[ 
            "title",
            "address",
            "city",
            "description",
            "price",
            "area",
            "floor",
            "bedrooms",
            "kitcheen",
            "bathrooms",
            "garage",
            "AirCondition",
            "ComunityCenter",
            "SecuritySystem",
            "Furniture",
            "list_date",
            "photo_main",
            "photo_1",
            "photo_2",
            "photo_3",
            "photo_4",
            "photo_5",
            "status",
        ]
        
        

