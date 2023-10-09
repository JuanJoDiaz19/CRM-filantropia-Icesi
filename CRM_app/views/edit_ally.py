from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from CRM_app.models import Allie,Allie_Type,ContactInfo, Area
import base64

class EditAlly(View):
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
            
            areas = Area.objects.all() 
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

            contact_name = request.POST.get('contact_name', '')
            contact_document_id = request.POST.get('contact_document_id', '')
            contact_phone = request.POST.get('contact_phone', '')
            contact_email = request.POST.get('contact_email', '')
            contact_aux_email = request.POST.get('contact_aux_email', '')

            # Check if the updated ally type exists
            if allie_type_string in ['juridica', 'natural']:
                allie_type = Allie_Type.objects.get(name=allie_type_string)
                ally.allie_type_id = allie_type

            # Check if an image was uploaded and update the image_link
            if ally_image:
                try:
                    allie_image_link = base64.b64encode(ally_image.read()).decode('utf-8')
                    ally.image_link = allie_image_link
                except FileNotFoundError:
                    # Handle the case where the new image does not exist
                    pass
            else:
                # Handle the case where no new image is provided
                # In this case, keep the existing image link
                allie_image_link = ally.image_link


            ally.save()

            for contact in contact_info:
                contact.name = request.POST.get('contact_name', contact.name)
                
                
            for contact_info_id in request.POST.getlist('id'):
                print(contact_info_id.name)    
            

            for contact_info_id in request.POST.getlist('id'):
                if contact_info_id:
                    try:
                        contact_info = ContactInfo.objects.get(id=contact_info_id)
                    except ContactInfo.DoesNotExist:
                        contact_info = None
                        
                else:
                    contact_info = None

                # Create a ContactInfoForm for each contact_info object
               

            # Delete removed contact info
            contact_info_ids_to_delete = request.POST.getlist('contact_info_delete')
            ContactInfo.objects.filter(id__in=contact_info_ids_to_delete).delete()

            return redirect(f'/allies/{allie_id}/')