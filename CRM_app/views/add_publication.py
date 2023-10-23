from django.shortcuts import render, redirect
from django.views import View
from CRM_app.models import Allie_Type, Allie, ContactInfo, Donation_Type, Donation, Publication,Investigation_Project
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.urls import reverse

class AddPublication(View):
    @method_decorator(login_required)
    def get(self, request,project__id):
        try:
            project = Investigation_Project.objects.get(id=project__id)
        except Publication.DoesNotExist:
            project = None
        return render(request, 'add-publication.html',{'project': project})
    
    @method_decorator(login_required)
    def post(self, request, project__id):
        
        project = Investigation_Project.objects.get(id=project__id)
        
        
        publicacion_nombre= request.POST.get('nombre', False)
        publicacion_date= request.POST.get('fecha',False)
        publicacion_description= request.POST.get('descripcion',False)
        
        if not (publicacion_nombre and publicacion_date and publicacion_description):
            return render(request, 'add-publication.html',{'error_message': "Datos inválidos",'project': project})
        
        Publication.objects.create(
            name=publicacion_nombre,
            date=publicacion_date,
            doi=publicacion_description,
            investigation_project_id=project
        )
        
        return redirect(f'/investigation/{project__id}')

        

        