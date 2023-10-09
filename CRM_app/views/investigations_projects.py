from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login,logout, authenticate
from CRM_app.models import Investigation_Project
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q

class InvestigationsProjects(View):
    @method_decorator(login_required)
    def get(self, request):
        query = request.GET.get('q', '').strip()
        investigation_projects = Investigation_Project.objects.all() 

        if query != "":
            investigation_projects = investigation_projects.filter(Q(name__istartswith=query))

        return render(request, 'investigation_projects.html', {'investigation_projects': investigation_projects})
    