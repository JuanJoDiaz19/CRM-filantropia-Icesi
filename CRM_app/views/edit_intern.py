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
            careers = [{'id': str(career.id), 'name': career.name} for career in careers]
            
            return render(request, 'edit_intern.html', {'ally': allie_id,'practicing':practicing,'careers': careers})  
               


    def post(self, request, allie_id, contact_info_id):
        try:
            # Obtén el objeto Allie y ContactInfo correspondientes a los IDs proporcionados
            ally = Allie.objects.get(id=allie_id)
            contact_info = ContactInfo.objects.get(id=contact_info_id)
        except Allie.DoesNotExist:
            # Maneja el caso en el que el aliado no existe
            ally = None
            contact_info = None
        except ContactInfo.DoesNotExist:
            # Maneja el caso en el que la información de contacto no existe
            contact_info = None
        
        if request.method == 'POST':
            if 'delete' in request.POST:
                if contact_info:
                    contact_info.delete()
                # Redirige a alguna página de éxito o a donde necesites
                return redirect(f'/allies/{allie_id}/')
            elif 'edit' in request.POST:
                # Actualiza los campos de ContactInfo con los datos del formulario
                if contact_info:
                    contact_info.name  = request.POST.get('contact_name', '')
                    contact_info.phone_number  = request.POST.get('contact_phone', '')
                    contact_info.email = request.POST.get('contact_email', '')
                    contact_info.aux_email = request.POST.get('contact_aux_email', '')
                    
                    contact_info.save()
                # Redirige a alguna página de éxito o a donde necesites
                return redirect(f'/allies/{allie_id}/')
   


            