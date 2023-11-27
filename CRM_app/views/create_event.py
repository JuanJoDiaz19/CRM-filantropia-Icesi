from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from CRM_app.models import Allie, Event_Type, EventAllie,Event,New
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
        event_name= request.POST.get('nombre', False)
        event_allie= request.POST.getlist('countries[]', False)
        event_type= request.POST.get('categoria', False)
        event_objective= request.POST.get('allie_area', False)
        event_description= request.POST.get('allie_description', False)
        event_fecha= request.POST.get('fecha',False)
        
        if not (event_name and event_allie and event_type and event_objective and event_description and event_fecha):
            allies= Allie.objects.all()
            event_type= Event_Type.objects.all()
            return render(request, 'create_event.html', {'error_message': "Proporcione todos los datos",'allies': allies,'event_type': event_type})
        
        #print(event_allie, '\n')
       
        #for i in event_allie:
            #print(i)
        event_type_instance= get_object_or_404(Event_Type,id=event_type)
        
        event_create=Event.objects.create(
                event_type_id= event_type_instance,
                date= event_fecha,
                name=event_name,
                objective=event_objective,
                description= event_description,
            )
        
        New.objects.create(
                title = "el evento " + event_name + " se realizara el " + event_fecha ,
                description="",
                date= event_fecha
        )
        
        ally=[]
        for i in event_allie: 
            allyget= get_object_or_404(Allie,id=i)
            ally.append(allyget)
        
        for all in ally:
            EventAllie.objects.create(
                event= event_create,
                allie= all,
            )
        
        return redirect('/calendar/all')