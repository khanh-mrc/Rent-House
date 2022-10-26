from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from .models import *
from .forms import OrderForm, CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#  Create your views here.

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else: 
            messages.info(request, 'Username or Password is Incorrect')
            #return render(request,"login.html",login.html)
    context ={
        
    }
    return render(request,'accounts/login.html',context)

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            # Check username
            if User.objects.filter(username = username).exists():
                messages.error(request,'"'+username + '" already exists. Please try another username')
                return redirect('register')
            else:
                if User.objects.filter(email = email).exists():
                    messages.error(request,'Email "' + email+'" already exists. Please try another email')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username = username,
                    password = password1,email=email,first_name = first_name,
                    last_name = last_name)
                    user.save()
                    messages.success(request,  'Account was created for "'+ username +'"')
                    return redirect('login')
        else:
            messages.error(request,'Password and confirm password does not match')
            return redirect('register')
    else:
        return render(request,'accounts/register.html')
#   form =  CreateUserForm()
        '''
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username = username).exists():
            messages.error(request,"That username is exist.")
            return render(request,'accounts/register1.html')
        else:
            user = User.objects.create_user(username=username, password=password1, email= email, first_name=first_name, last_name=last_name)
            user.save()
        #print('user created')
            usern = user.cleaned_data.get('username')
            messages.success(request,  'Account was created for ')
            return redirect('login')
            '''
    #else:
        #return render('accounts/register1.html')
        '''
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,  'Account was created for '+ user)
            return redirect('login')
    context={
        'form':form
    }
    return render(request,'accounts/register1.html',context)
    '''

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login' )
def dashboard(request):
    context={
    }
    return render(request,'accounts/dashboard.html',context)

