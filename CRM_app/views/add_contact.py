from django.shortcuts import render, redirect
from django.views import View
from CRM_app.models import Allie_Type, Allie, ContactInfo
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest

class AddContact(View):
    @method_decorator(login_required)
    def post(self, request, allie_id):
        allie = Allie.objects.get(id=allie_id)
        contact_info = ContactInfo.objects.filter(allie=allie_id)

        contact_name = request.POST.get('contact_name', False)
        contact_document_id = request.POST.get('contact_document_id', False)
        contact_phone = request.POST.get('contact_phone', False)
        contact_email = request.POST.get('contact_email', False)
        contact_aux_email = request.POST.get('contact_aux_email', False)

        existing_contact = ContactInfo.objects.filter(id=contact_document_id, allie=allie)

        if not (contact_name and contact_document_id and contact_phone and contact_email):
            return render(request, 'allies/single-page-ally.html', {'error_message': "Datos inválidos",'allies': allie,'contact_info': contact_info})
        
        if existing_contact.exists():
            return render(request, 'allies/single-page-ally.html', {'error_message': "Un contacto con el mismo documento ya existe",'allies': allie,'contact_info': contact_info})

        ContactInfo.objects.create(
            id=contact_document_id,
            email=contact_email,
            phone_number=contact_phone,
            aux_email=contact_aux_email,
            name=contact_name,
            allie=allie
        )
        
        return render(request, 'allies/single-page-ally.html', {'allies': allie, 'contact_info': contact_info})
