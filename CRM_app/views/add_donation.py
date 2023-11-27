from django.shortcuts import render, redirect
from django.views import View
from CRM_app.models import Allie_Type, Allie, ContactInfo, Donation_Type, Donation, New
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

class AddDonation(View):
    @method_decorator(login_required)
    def get(self, request,allie__id):
        try:
            ally = Allie.objects.get(id=allie__id)
        except Allie.DoesNotExist:
            ally = None
        return render(request, 'allies/add-donation.html',{'ally': ally})
    
    @method_decorator(login_required)
    def post(self, request, allie__id):
        donation_date= request.POST.get('fecha',False)
        donation_amount= request.POST.get('nombre', False)
        donation_description= request.POST.get('descripcion', False)
        donations_types= Donation_Type.objects.all()
        
        if donation_date and donation_amount:
            try:
                amount_number= int(donation_amount)
            except ValueError:
                try:
                    ally = Allie.objects.get(id=allie__id)
                except Allie.DoesNotExist:
                    ally = None
                return render(request, 'allies/add-donation.html', {'error_message': "En este campo solo pueden ir valores númericos",'ally': ally })
            
            allie_instance= get_object_or_404(Allie, id= allie__id)
            
            for types in donations_types:
                if(amount_number<0):
                    return render(request, 'allies/add-donation.html', {'error_message': "No puede poner un monto tan pequeño"})
                elif(amount_number>=types.min_value and amount_number<types.max_value):
                    donation_type_instance= get_object_or_404(Donation_Type, id=types.id)
                    break
                else:
                    donation_type_instance= get_object_or_404(Donation_Type,id=types.id)
                
            Donation.objects.create(
                date=donation_date,
                amount = amount_number,
                donation_type_id= donation_type_instance,
                allie_id= allie_instance,
                description= donation_description,
            )
    
            New.objects.create(
                title = allie_instance.name + " acaba de hacer una donación de " + str(amount_number)
,
                description="",
                date= donation_date
            )
            
            return redirect(f'/donations/{allie__id}')
        else:
            try:
                ally = Allie.objects.get(id=allie__id)
            except Allie.DoesNotExist:
                ally = None
            return render(request, 'allies/add-donation.html', {'error_message': "Faltan campos necesarios para el registro",'ally': ally })