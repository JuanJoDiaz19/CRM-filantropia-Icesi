from django.shortcuts import render, redirect
from django.views import View
from CRM_app.models import Allie, Investigation_Project, AllieProject, Publication

class InvestigationProject(View):
    def get(self, request, project__id):    
        
        try:
            proyecto_investigacion = Investigation_Project.objects.get(id=project__id)
        except Investigation_Project.DoesNotExist:
            proyecto_investigacion=None
        
        try:
            aliados_del_proyecto = AllieProject.objects.filter(investigation_project=proyecto_investigacion)
        except AllieProject.DoesNotExist:
            aliados_del_proyecto=[]
        
        try:
            publication= Publication.objects.filter(investigation_project_id=project__id)
        except Publication.DoesNotExist:
            publication=[]
            
        

         
        return render(request, 'single_page_investigation_projects.html',{'projects': aliados_del_proyecto, 'project': proyecto_investigacion, 'publications': publication})