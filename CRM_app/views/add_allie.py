from django.shortcuts import render, redirect
from django.views import View
from CRM_app.models import Allie_Type, Allie, ContactInfo, Area
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

import datetime
import os
import base64

class Add_allie(View):
    @method_decorator(login_required) 
    def get(self, request):
        areas = Area.objects.all() 
        areas = [{'id': str(area.id), 'name': area.area_description} for area in areas]
        return render(request, 'add_allie.html',{'areas': areas})

    @method_decorator(login_required) 
    def post(self, request):
        
        allie_name = request.POST.get('allie_name', False)
        allie_document_id = request.POST.get('allie_document_id', False)
        allie_area = request.POST.get('allie_area', False)
        allie_description = request.POST.get('allie_description', False) 
        allie_type_string = request.POST.get('allie_type', False) 
        allie_image_temp = request.POST.get('image2', False) 
        allie_image = request.FILES.get('image', None)

        contact_name = request.POST.get('contact_name', False)
        contact_document_id = request.POST.get('contact_document_id', False)
        contact_phone = request.POST.get('contact_phone', False)
        contact_email = request.POST.get('contact_email', False)
        contact_aux_email = request.POST.get('contact_aux_email', False)
        

        
        areas = Area.objects.all() 
        areas = [{'id': str(area.id), 'name': area.area_description} for area in areas]
        allie_area_name = Area.objects.filter(id=allie_area)[0].area_description
        
        if allie_image:
            allie_image_link = base64.b64encode(allie_image.read()).decode('utf-8')
        else:
            image_path = "CRM_app\static\img\home\profile.png"
            with open(image_path, 'rb') as image_file:
                image_binary = image_file.read()
            allie_image_link  = base64.b64encode(image_binary).decode('utf-8')
        
        
        context = {
            'allie_name': allie_name,
            'allie_document_id': allie_document_id,
            'allie_area': allie_area,
            'allie_area_name': allie_area_name,
            'allie_description': allie_description,
            'allie_type_string': allie_type_string,
            'allie_image': allie_image_link,
            'contact_name': contact_name,
            'contact_document_id': contact_document_id,
            'contact_phone': contact_phone,
            'contact_email': contact_email,
            'contact_aux_email': contact_aux_email,
            'areas':areas
        }
        
        

        if allie_name and allie_document_id and allie_area and allie_type_string and contact_name and contact_document_id and contact_phone and contact_email:
            if allie_type_string == "juridica" or allie_type_string == "natural":

                if Allie.objects.filter(id=allie_document_id).exists():
                    return render(request, 'add_allie.html', {'error_message': "Ya existe un aliado con este documento"})
                    

                allie_index = 0

                if allie_type_string == "juridica":
                    allie_index = 1
                elif allie_type_string == "natural":
                    allie_index = 2
                
                allie_type = Allie_Type.objects.get(id=allie_index)
                
                new_allie = Allie.objects.create(
                    id = allie_document_id,
                    allie_type_id=allie_type,
                    name=allie_name,
                    area_id=Area.objects.get(id=allie_area),
                    description=allie_description,
                    image_link=allie_image_link
                )

                ContactInfo.objects.create(
                    id = contact_document_id,
                    email = contact_email,
                    phone_number = contact_phone,
                    aux_email = contact_aux_email,
                    name = contact_name,
                    allie = new_allie
                )


                return redirect('allies')
            else:
                context['error_message'] = "Mensaje de error"
                return render(request, 'add_allie.html', context)
        else:
            context['error_message'] = "Proporcione todos los datos"
            return render(request, 'add_allie.html', context)
