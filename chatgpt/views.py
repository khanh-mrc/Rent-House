from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
# Create your views here.
from dotenv import load_dotenv
import os
import openai
from .models import ChatGptBot
load_dotenv()
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages

openai.api_key = os.getenv("OPENAI_API_KEY")




def chatgpt(request):
    #check if user is authenticated
    if request.user.is_authenticated:
        if request.method == 'POST':
            #get user input from the form
            user_input = request.POST.get('userInput')
            #clean input from any white spaces
            clean_user_input = str(user_input).strip()
            #send request with user's prompt
            response = openai.Completion.create(
                model="text-davinci-003",
                    prompt=clean_user_input,
                    temperature=0,
                    max_tokens=1000,
                    top_p=1,
                    frequency_penalty=0.5,
                    presence_penalty=0
                    )
            #get response
            bot_response = response['choices'][0]['text']
            
            obj, created = ChatGptBot.objects.get_or_create(
                user=request.user,
                messageInput=clean_user_input,
                bot_response=bot_response.strip(),
            )
            return redirect(request.META['HTTP_REFERER'])
        else:
            #retrieve all messages belong to logged in user
            get_history = ChatGptBot.objects.filter(user=request.user)
            context = {'get_history':get_history}
            return render(request, 'chatgpt/chatgpt.html', context)
    else:
        messages.error(request, 'Please Login to Use  Chat GPT!')
        return redirect("home")


@login_required
def DeleteHistory(request):
    chatGptobjs = ChatGptBot.objects.filter(user = request.user)
    chatGptobjs.delete()
    return redirect(request.META['HTTP_REFERER'])
