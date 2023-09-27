from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from CRM_app.models import Allie,Allie_Type,ContactInfo

class Ally(View):
    def get(self, request, allie_id):
            try:
                ally = Allie.objects.get(id=allie_id)
            except Allie.DoesNotExist:
                # Puedes manejar aquí el caso en el que el aliado no exista
                ally = None
                
            try :
                contact_info= ContactInfo.objects.filter(allie=allie_id)
            except ContactInfo.DoesNotExist:
                contact_info= []
             
            #contact_info= ContactInfo.objects.all()
                
            return render(request, 'allies/single-page-ally.html',{'allies':ally, 'contact_info': contact_info})
        

        
            
    
    