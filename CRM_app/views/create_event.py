from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from CRM_app.models import Allie, Event_Type, EventAllie,Event
from django.shortcuts import get_object_or_404

import datetime
import os
import base64

class create_event(View):
    def get(self, request):
        
        allies= Allie.objects.all()
        event_type= Event_Type.objects.all()
        
        return render(request, 'create_event.html',{
            'allies': allies,
            'event_type': event_type
        })
        
    def post(self, request):
        
        event_image= request.FILES.get('image', None)
        event_name= request.POST.get('allie_name', False)
        event_allie= request.POST.get('allie', False)
        event_type= request.POST.get('categoria', False)
        event_objective= request.POST.get('allie_area', False)
        event_description= request.POST.get('Objective', False)
        event_fecha= request.POST.get('fecha',False)
        
        event_type_instance= get_object_or_404(Event_Type,id=event_type)
        event_image_link=base64.b64encode(event_image.read()).decode('utf-8')
        
        event_create=Event.objects.create(
                event_type_id= event_type_instance,
                date= event_fecha,
                name=event_name,
                objective=event_objective,
                description= event_description,
                image_link= event_image_link,
            )
        
        ally= get_object_or_404(Allie,id=event_allie)
        
        EventAllie.objects.create(
            event= event_create,
            allie= ally,
        )
        
        return redirect('/allies')