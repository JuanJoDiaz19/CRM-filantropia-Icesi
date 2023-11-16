from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from CRM_app.models import New

class Cedep_marketing_home(View):
    def get(self, request):
        news = New.objects.all()
        return render(request, 'CEDEP_Marketing/CEDEP_marketing_home.html', {'news': news})