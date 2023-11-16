from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from CRM_app.models import Allie, Meeting_type, Meeting
from django.shortcuts import get_object_or_404

class create_meeting(View):
    def get(self, request):
        
        allies= Allie.objects.all()
        mt= Meeting_type.objects.all()
        
        return render(request, 'create_meeting.html',{'allies':allies,'mt':mt})
    
    def post(self, request):
        meeting_name= request.POST.get('nombre',False)
        meeting_categoria= request.POST.get('categoria', False)
        meeting_aliado= request.POST.get('ally',False)
        meeting_objetive= request.POST.get('objetivo',False)
        meeting_description= request.POST.get('description',False)
        meeting_date= request.POST.get('fecha', False)
        
        category_instance= get_object_or_404(Meeting_type, id= meeting_categoria)
        ally_instance= get_object_or_404(Allie,id=meeting_aliado)
        
        Meeting.objects.create(
            allie_id= ally_instance,
            meeting_type_id= category_instance,
            date= meeting_date,
            title=meeting_name,
            description= meeting_description,
            objective= meeting_objetive,
        )
        
        return redirect('/calendar/all')
        