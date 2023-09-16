from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout 
from django.db import IntegrityError
from .models import New
from .forms import NewForm


# Create your views here.
 
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
         return render(request, 'signup.html', {
        'form': UserCreationForm
    })

    else : 
        if(request.POST['password1'] == request.POST['password2']):
            # Register User
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
    
def tasks(request):
    return render(request, 'tasks.html')

def sing_out(request):
    logout(request)
    return redirect('home')
    
def news(request):
    news = New.objects.all()  # Obtener todas las instancias de New
    return render(request, 'news.html', {'news': news})

def create_new(request):
    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
    else:
        form = NewForm()

    return render(request, 'create_new.html', {'form': form})

def delete_new(request, new_id):
    new = New.objects.get(id=new_id)
    new.delete()
    return redirect('news')
   
