from django.shortcuts import render, redirect
from django.views import View
from CRM_app.models import Allie_Type, Allie
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
        name = request.POST.get('allie_name', False)
        document_id = request.POST.get('allie_document_id', False)
        area = request.POST.get('allie_area', False)
        description = request.POST.get('allie_description', False) 
        allie_type_string = request.POST.get('allie_type', False) 
        image = request.FILES['image']

        blob = bucket.blob(f'allie_images/{image.name}')
        blob.upload_from_file(image, content_type=image.content_type)

        expiration = datetime.timedelta(days=1)
        token = blob.generate_signed_url(expiration=expiration, version='v4')

        allie_index = 0

        if allie_type_string == "juridica":
            allie_index = 1
        elif allie_type_string == "natural":
            allie_index = 2
        
        allie_type = Allie_Type.objects.get(id=allie_index)
        
        Allie.objects.create(
            allie_type_id=allie_type,
            name=name,
            area=area,
            description=description,
            image_link=token
        )

        return redirect('allies')
