from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages
from CRM_app.models import Allie, Investigation_Project, AllieProject
from django.shortcuts import get_object_or_404

class AddInvestigationProject(View):
    def get(self, request):
        allies= Allie.objects.all()
        return render(request, 'add_investigation_project.html',{'allies': allies})
    
    def post(self, request):
        project_title= request.POST.get('titulo', False)
        project_allies= request.POST.getlist('allies[]', False)
        project_date= request.POST.get('fecha',False)
        project_description= request.POST.get('descripcion',False)
        project_objetivos= request.POST.get('objetivos',False)
        
        
        project = Investigation_Project.objects.create(
            name=project_title,
            description=project_description,
            active=True,
            start_date=project_date,
            objetivos=project_objetivos
        )
        
        for prj in project_allies:
            pr=get_object_or_404(Allie, id=prj)
            AllieProject.objects.create(
                investigation_project= project,
                allie= pr
            )
        
            
            
        return redirect('/investigations')