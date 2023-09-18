from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError

class Singin(View):
    def get(self, request):
        return render(request, 'signin.html', {
        'form' : AuthenticationForm
    })
    
    def post(self, request):
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
            'form' : AuthenticationForm, 
            'error': 'Username or Password is incorrect'
            })
        else:
            login(request, user)
            return redirect('tasks')
    
    