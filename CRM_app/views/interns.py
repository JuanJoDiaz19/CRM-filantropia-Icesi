from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from CRM_app.models import Practicing, Allie
from django.db.models import Q

class Interns(View):
    def get(self, request, allie__id):
        
        query = request.GET.get('q', '').strip()
        
        try:
            practicing= Practicing.objects.filter(allie_id=allie__id)
        except Practicing.DoesNotExist:
            practicing=[]
        
        if query!="":
            practicing= practicing.filter(Q(name__istartswith=query))
        
        try: 
            ally= Allie.objects.get(id=allie__id)
        except Allie.DoesNotExist:
            ally=[]
            
        return render(request, 'interns.html', {'practice':practicing, 'ally':ally})