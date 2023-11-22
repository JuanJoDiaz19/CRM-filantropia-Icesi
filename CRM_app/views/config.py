from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from CRM_app.models import Donation_Type
import base64

class Config(View):
    
    @method_decorator(login_required)
    def get(self, request):
        donation_types = Donation_Type.objects.all()
        donation_types_count = donation_types.count() 
        letra = chr(65 + donation_types_count) 
        return render(request, 'config.html', {
        'donation_types': donation_types,
        'letra': letra
    })
    
    
    @method_decorator(login_required)
    def post(self, request):
        image = request.FILES.get('image')
        if image is None:
            donation_types = Donation_Type.objects.all()
            donation_types_count = donation_types.count() 
            letra = chr(65 + donation_types_count) 

            # Solo procede si hay objetos Donation_Type
            if donation_types.exists():
                ranges = []  # Lista para almacenar tuplas (min_value, max_value) de los Donation_Type existentes

                for donation_type in donation_types:
                    ranges.append((donation_type.min_value, donation_type.max_value))
                    
                min_value_new= request.POST.get('source', False)
                max_value_new= request.POST.get('destination', False)
                min_value_new= int(min_value_new) if min_value_new else None
                max_value_new= int(max_value_new) if max_value_new else None
                
                new_range = (min_value_new, max_value_new)
                print(new_range)
                print(ranges)
                
                if min_value_new is not None and max_value_new is not None:
                    if min_value_new >= max_value_new:
                        return render(request, 'config.html', {
                            'donation_types': donation_types,
                            'letra': letra,
                            'message': 'min_value debe ser menor que max_value'
                        })

                            
                for existing_range in ranges:
                    if (new_range[0] >= existing_range[0] and new_range[0] < existing_range[1]) or \
                        (new_range[1] >= existing_range[0] and new_range[1] <= existing_range[1]):
                            return render(request, 'config.html', {
                            'donation_types': donation_types,
                            'letra': letra,
                            'message': 'Los rangos no pueden solaparse'
                            })
                
                for donation_type in donation_types:
                    min_value_raw = request.POST.get(f'min_value_{donation_type.id}', '').strip()
                    max_value_raw = request.POST.get(f'max_value_{donation_type.id}', '').strip()
                    

                    try:
                        min_value = int(min_value_raw) if min_value_raw else None
                        max_value = int(max_value_raw) if max_value_raw else None
                        
                        
                                #raise ValidationError("min_value debe ser menor que max_value")
                            
                            
                                    


                            
                        if min_value is not None and max_value is not None:
                            donation_type.min_value = min_value
                            donation_type.max_value = max_value
                            donation_type.save()
                                
                            ranges.append(new_range)
                    except ValueError:
                        # Aquí puedes manejar los errores de conversión, por ejemplo, registrando un mensaje de error
                        pass

            nombre= request.POST.get('name_donation', False)
            if nombre is not False:
                min_value_new= request.POST.get('source', False)
                max_value_new= request.POST.get('destination', False)
                try: 
                    if min_value_new is not None and max_value_new is not None:
                        Donation_Type.objects.create(
                            max_value= max_value_new,
                            min_value = min_value_new,
                            name= nombre,
                        )
                except ValueError:
                # Maneja el caso en el que la conversión a entero falle
                # Aquí puedes agregar lógica para manejar valores no válidos
                    pass
            
            
            return redirect('/config')
            
        else:
            image_link = base64.b64encode(image.read()).decode('utf-8')
            user = request.user
            user.image_link = image_link  
            user.save()
            
            
        
        return redirect('/config')


        