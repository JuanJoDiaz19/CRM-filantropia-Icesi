from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages

class Singin(View):
    def get(self, request):
        return render(request, 'signin.html', {
        'form' : AuthenticationForm
    })
    
    def post(self, request):
        print(request)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is None:
            messages.success(request, ("There was an error login i, try again"))
            redirect('singin')
        else:
            login(request, user) 
            return redirect('tasks')
    
    