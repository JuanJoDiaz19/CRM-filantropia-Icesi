from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from CRM_app.models import Allie,Allie_Type,ContactInfo, Area
from django.contrib import messages
import base64

class EditAlly(View):
    def get(self, request, allie_id):
            try:
                ally = Allie.objects.get(id=allie_id)
            except Allie.DoesNotExist:
                ally = None
                
            try :
                contact_info= ContactInfo.objects.filter(allie=allie_id)
            except ContactInfo.DoesNotExist:
                contact_info= []
            
            areas = Area.objects.all() 
            areas = Area.objects.exclude(id=ally.area_id.id)
            areas = [{'id': str(area.id), 'name': area.area_description} for area in areas]
                
            return render(request, 'allies/edit_ally.html',{'allies':ally, 'contact_info': contact_info,'areas': areas})
    
    def post(self, request, allie_id):
            try:
                ally = Allie.objects.get(id=allie_id)
                contact_info= ContactInfo.objects.filter(allie=allie_id)
            except Allie.DoesNotExist:
                ally = None

            # Retrieve and update ally data from the POST request
            ally.name = request.POST.get('allie_name', ally.name)
            
            allie_area = request.POST.get('allie_area', False)
            ally.area_id=Area.objects.get(id=allie_area)
            
            ally.description = request.POST.get('allie_description', ally.description)
            allie_type_string = request.POST.get('allie_type', ally.allie_type_id)
            ally_image = request.FILES.get('image')



            if allie_type_string in ['juridica', 'natural']:
                allie_type = Allie_Type.objects.get(name=allie_type_string)
                ally.allie_type_id = allie_type

            if ally_image:
                try:
                    allie_image_link = base64.b64encode(ally_image.read()).decode('utf-8')
                    ally.image_link = allie_image_link
                except FileNotFoundError:

                    pass
            else:
                allie_image_link = ally.image_link


            ally.save()
            messages.success(request, "Editado con éxito")
            return redirect(f'/allies/{allie_id}/')