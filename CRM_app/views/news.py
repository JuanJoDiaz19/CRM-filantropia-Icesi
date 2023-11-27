from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from CRM_app.models import New, User

class News(View):
    def get(self, request):
        latest_news = New.objects.all().order_by('-date')[:10]
        
        return render(request, 'news.html', {'news': latest_news})