from django.shortcuts import render
from django.views import View
from CRM_app.models import Allie, Allie_Type, User
from django.db.models import Q
from django.contrib.auth.decorators import login_required



class Allies(View):
    def get(self, request):
        
        query = request.GET.get('q', '').strip()
        state = request.GET.get('estado', '')
        type_id = request.GET.get('tipo', '')

        if state == 'activo':
            allies = Allie.objects.filter(active=True)
        elif state == 'inactivo':
            allies = Allie.objects.filter(active=False)
        else:
            allies = Allie.objects.all()

        if query != "":
            allies = allies.filter(Q(name__istartswith=query))
        if type_id:
            allies = allies.filter(allie_type_id=type_id)

        allie_types = Allie_Type.objects.all() 
        allie_types = [{'id': str(allie_type.id), 'name': allie_type.name} for allie_type in allie_types]
        user= User.object.all()

        return render(request, 'allies.html', {'allies': allies, 'allie_types': allie_types,'user': user})


