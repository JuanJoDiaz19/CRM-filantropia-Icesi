from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from CRM_app.models import Allie,Allie_Type,ContactInfo, Practicing, Career
import base64

class EditIntern(View):
    def get(self, request, allie_id,intern_id):
            
            try :
                interns= Practicing.objects.filter(id=intern_id)
                practicing = interns[0]
            except Practicing.DoesNotExist:
                practicing=None
             
            #contact_info= ContactInfo.objects.all()
            careers = Career.objects.all() 
            careers = Career.objects.exclude(id=practicing.career_id.id)
            careers = [{'id': str(career.id), 'name': career.name} for career in careers]
            
            return render(request, 'edit_intern.html', {'ally': allie_id,'practicing':practicing,'careers': careers})  
               


    def post(self, request, allie_id, intern_id):
        try:
            # Obtén el objeto Allie y ContactInfo correspondientes a los IDs proporcionados
            ally = Allie.objects.get(id=allie_id)
            practicing = Practicing.objects.get(id=intern_id)
        except Allie.DoesNotExist:
            # Maneja el caso en el que el aliado no existe
            ally = None
            practicing = None
        except ContactInfo.DoesNotExist:
            # Maneja el caso en el que la información de contacto no existe
            practicing = None
        intern_image = request.FILES.get('image')    
        
            
        
        if request.method == 'POST':
            if 'delete' in request.POST:
                if practicing:
                    practicing.delete()
                # Redirige a alguna página de éxito o a donde necesites
            
            elif 'edit' in request.POST:
                # Actualiza los campos de ContactInfo con los datos del formulario
                if practicing:
                    
                    if intern_image:
                        try:
                            intern_image_link = base64.b64encode(intern_image.read()).decode('utf-8')
                            practicing.image_link = intern_image_link
                        except FileNotFoundError:
                            pass
                    
                    career = request.POST.get('allie_area', False)
                    
                    
                    practicing.name  = request.POST.get('nombre', '')
                    practicing.career_id  = Career.objects.get(id=career)
                    practicing.position = request.POST.get('allie_description', '')
                    
                    practicing.save()
                # Redirige a alguna página de éxito o a donde necesites
                   
        
        return redirect(f'/interns/{allie_id}')
   

            