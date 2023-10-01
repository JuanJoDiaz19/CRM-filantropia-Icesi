from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from CRM_app.models import Practicing, Gender, Career, Allie
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404

import datetime
import os
import firebase_admin 
from firebase_admin import credentials, storage

if not firebase_admin._apps:
    cred = credentials.Certificate('crm-app-filantropia-icesi-firebase-adminsdk-6isgm-16b172ef8f.json') 
    default_app = firebase_admin.initialize_app(cred, {'storageBucket': 'crm-app-filantropia-icesi.appspot.com'})
    
bucket = storage.bucket()

class Add_intern(View):
    @method_decorator(login_required)
    def get(self, request, allie__id):
        return render(request, 'add_intern.html', {'ally': allie__id})
    
    @method_decorator(login_required)
    def post(self, request, allie__id):
        intern_name= request.POST.get('nombre',False)
        intern_id= request.POST.get('allie_document_id',False)
        intern_carrera= request.POST.get('allie_area',False)
        intern_position= request.POST.get('allie_description',False)
        sex= request.POST.get('sex',False)
        image=  request.FILES.get('image', None)
       
        if intern_name and intern_id and intern_carrera and intern_position and sex:
        
            allie_instance = get_object_or_404(Allie, id=allie__id)
            career_instance= get_object_or_404(Career,id=intern_carrera)
            gender_instace= get_object_or_404(Gender,id=sex)
            
            if Practicing.objects.filter(id=intern_id).exists():
                return render(request, 'add_intern.html', {'error_message': "Ya existe un practicante con este documento"})
            
            blob = bucket.blob(f'practicing_images/{image.name}')
            blob.upload_from_file(image, content_type=image.content_type)

            allie_image_link = blob.public_url

            
            Practicing.objects.create(
                id= intern_id,
                allie_id=allie_instance,
                name= intern_name,
                position= intern_position,
                career_id= career_instance,
                gender_id= gender_instace,  
                image_link=allie_image_link,
            )
            
            return redirect('/allies')
        else:
            return render(request,'add_intern.html',{'error_message': "Proporcione todos los datos"})
    
        