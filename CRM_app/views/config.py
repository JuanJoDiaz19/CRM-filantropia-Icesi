from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from CRM_app.models import Donation_Type

class Config(View):
    
    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'config.html')
    
    
    @method_decorator(login_required)
    def post(self, request):
        source1_range= request.POST.get('source1', False)
        destination1_range= request.POST.get('destination1', False)
        source2_range= request.POST.get('source2', False)
        destination2_range= request.POST.get('destination2', False)
        source3_range= request.POST.get('source3', False)
        destination3_range= request.POST.get('destination3', False)
        
      
        
        Donation_Type.objects.create(
            max_value= destination1_range,
            min_value = source1_range,
            name= 'C',
        )
        
        Donation_Type.objects.create(
            max_value= destination2_range,
            min_value = source2_range,
            name= 'B',
        )    
        
        Donation_Type.objects.create(
            max_value= destination3_range,
            min_value = source3_range,
            name= 'A',
        )
        
        return redirect('/home')