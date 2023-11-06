from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages


class LogIn(View):
    def get(self, request):
        return render(request, 'login.html')
        
    def post(self, request):
        print(request.POST)
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {
                'message': 'El usuario o la contraseña son erroneos'
            })
        else:
            login(request, user)
            if user.is_superuser:
                return redirect('register')
            return redirect('home')
    
    