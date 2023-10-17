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
        project_allies= request.POST['allies']
        project_date= request.POST.get('fecha',False)
        project_description= request.POST.get('descripcion',False)
        
        projects_allies = [ally.strip() for ally in project_allies.split(',')]
        
        projects_allies_instances=[]
        
        print(project_allies)
        
        for prj in projects_allies:
            
            pr=get_object_or_404(Allie, id=prj)
            projects_allies_instances.append(pr)
        
        project = Investigation_Project.objects.create(
            name=project_title,
            description=project_description,
            active=True,
            start_date=project_date,
        )
        
        for ally in projects_allies_instances:
            AllieProject.objects.create(
                investigation_project= project,
                allie= ally
            )
            
        return redirect('/investigations')