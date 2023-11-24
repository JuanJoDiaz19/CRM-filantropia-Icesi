from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from CRM_app.models import New

class DeleteNew(View):
    def get(self, request, new_id):
        new = New.objects.get(id=new_id)
        new.delete()
        return redirect('news')