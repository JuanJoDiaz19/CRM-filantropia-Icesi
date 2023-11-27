from django.shortcuts import render, redirect
from django.views import View
from CRM_app.models import Allie
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseBadRequest
from django.contrib import messages

class SearchAlly(View):
    @method_decorator(login_required)
    def post(self, request):
        query = request.POST.get('q', '').strip()
        if query:
            try:
                ally = Allie.objects.get(name__iexact=query)
                return redirect(f'/reports/{ally.id}/')
            except Allie.DoesNotExist:
                messages.error(request, "Este aliado no existe")
                return redirect('/reports/')
        else:
            return HttpResponseBadRequest('No se proporcionó un término de búsqueda válido.')
