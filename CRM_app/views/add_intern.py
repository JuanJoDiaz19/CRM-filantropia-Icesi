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

class Add_intern(View):
    @method_decorator(login_required)
    def get(self, request, allie__id):
        return render(request, 'add_intern.html')
    
    @method_decorator(login_required)
    def post(self, request, allie__id):
        intern_name= request.POST['nombre']
        intern_id= request.POST['allie_document_id']
        intern_carrera= request.POST['allie_area']
        intern_position= request.POST['allie_description']
        sex= request.POST['sex']
       #allie__id= request.POST['allie__id']
        
        allie_instance = get_object_or_404(Allie, id=allie__id)
        career_instance= get_object_or_404(Career,id=intern_carrera)
        gender_instace= get_object_or_404(Gender,id=sex)

        
        Practicing.objects.create(
            id= intern_id,
            allie_id=allie_instance,
            name= intern_name,
            position= intern_position,
            career_id= career_instance,
            gender_id= gender_instace,  
        )
        
        return redirect('/allies')
    
        