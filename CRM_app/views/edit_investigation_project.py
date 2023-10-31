from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages
from CRM_app.models import Allie, Investigation_Project, AllieProject
from django.shortcuts import get_object_or_404
from datetime import datetime

class EditInvestigationProject(View):
    def get(self, request,project__id):
        try:
            project = Investigation_Project.objects.get(id=project__id)
        except Investigation_Project.DoesNotExist:
            project = None

        selected_allies=AllieProject.objects.filter(investigation_project=project__id)
        
        allies= Allie.objects.all()
        formatted_start_date = project.start_date.strftime('%Y-%m-%d')
        return render(request, 'edit_investigation_project.html',{'project': project,'allies': allies, 'selected_allies':selected_allies, 'formatted_start_date':formatted_start_date})
    
    
    def post(self, request,project__id):
        
        try:
            project = Investigation_Project.objects.get(id=project__id)
        except Investigation_Project.DoesNotExist:
            project = None
        
    
            
        if request.method == 'POST':
            if 'delete' in request.POST:
                if project:
                    project.delete()
                    messages.success(request, "Borrado con éxito")
                # Redirige a alguna página de éxito o a donde necesites
                return redirect(f'/investigations/')
            elif 'edit' in request.POST:
                
                project.name= request.POST.get('titulo', False)
                project_new_allies= request.POST.getlist('allies[]', False)
                project.start_date= request.POST.get('fecha',False)
                project.description= request.POST.get('descripcion',False)
                project.objetivos= request.POST.get('objetivos',False)
                        

                project.save()
                
                for new in project_new_allies:
                    pr=get_object_or_404(Allie, id=new)
                    AllieProject.objects.create(
                        investigation_project= project,
                        allie= pr
                    )
                
                
                #for ally in projects_allies_instances:
                #    AllieProject.objects.create(
                #        investigation_project= project,
                #        allie= ally
                #    )
                messages.success(request, "Editado con éxito")    
                return redirect('/investigations')