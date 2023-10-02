from django.shortcuts import render, redirect
from django.views import View
from CRM_app.models import Allie_Type, Allie, ContactInfo
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

import datetime
import os
import firebase_admin
from firebase_admin import credentials, storage

if not firebase_admin._apps:
    cred = credentials.Certificate('crm-app-filantropia-icesi-firebase-adminsdk-6isgm-16b172ef8f.json') 
    default_app = firebase_admin.initialize_app(cred, {'storageBucket': 'crm-app-filantropia-icesi.appspot.com'})


bucket = storage.bucket()

class AddAllie(View):
    @method_decorator(login_required) 
    def get(self, request):
        return render(request, 'add_allie.html')

    @method_decorator(login_required) 
    def post(self, request):
        
        allie_name = request.POST.get('allie_name', False)
        allie_document_id = request.POST.get('allie_document_id', False)
        allie_area = request.POST.get('allie_area', False)
        allie_description = request.POST.get('allie_description', False) 
        allie_type_string = request.POST.get('allie_type', False) 
        allie_image = request.FILES.get('image', None)

        contact_name = request.POST.get('contact_name', False)
        contact_document_id = request.POST.get('contact_document_id', False)
        contact_phone = request.POST.get('contact_phone', False)
        contact_email = request.POST.get('contact_email', False)
        contact_aux_email = request.POST.get('contact_aux_email', False)


        if allie_name and allie_document_id and allie_area and allie_type_string and allie_image and contact_name and contact_document_id and contact_phone and contact_email:
            if allie_type_string == "juridica" or allie_type_string == "natural":

                if Allie.objects.filter(id=allie_document_id).exists():
                    return render(request, 'add_allie.html', {'error_message': "Ya existe un aliado con este documento"})
            
                blob = bucket.blob(f'allie_images/{allie_image.name}')
                blob.upload_from_file(allie_image, content_type=allie_image.content_type)

                allie_image_link = blob.public_url

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
                    area=allie_area,
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
                return render(request, 'add_allie.html', {'error_message': "Datos invalidos"})
        else:
            return render(request, 'add_allie.html', {'error_message': "Proporcione todos los datos"})
