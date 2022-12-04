from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile


#from .models import Order
class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = '__all__'
		exclude = ['user']

class OrderForm(ModelForm):
    class Meta:
      #  model = Order
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email','username', 'password1', 'password2']