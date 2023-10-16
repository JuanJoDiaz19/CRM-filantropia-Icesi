from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages


class AddInvestigationProject(View):
    def get(self, request):
        return render(request, 'add_investigation_project.html')
    