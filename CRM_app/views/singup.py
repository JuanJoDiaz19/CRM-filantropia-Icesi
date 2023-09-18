from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError

class Singup(View):
    def get(self, request):
            return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    def post(self, request):
        if(request.POST['password1'] == request.POST['password2']):
            try: 
                user = User.objects.create_user(username = request.POST['username'], password = request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm, 
                    'error' : 'Username already exists'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm, 
            'error' : 'Password do not match'
        })
        
            
    
    