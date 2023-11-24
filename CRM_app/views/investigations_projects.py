from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login,logout, authenticate
from CRM_app.models import Investigation_Project, Allie, AllieProject
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q

class InvestigationsProjects(View):
    @method_decorator(login_required)
    def get(self, request):
        query = request.GET.get('q', '').strip()
        ally_id= request.GET.get('tipo', '')
        investigation_projects = Investigation_Project.objects.all() 

        if query != "":
            investigation_projects = investigation_projects.filter(Q(name__istartswith=query))
        if ally_id:
            try:
                allies_project= Allie.objects.get(id=ally_id)
            except Allie.DoesNotExist:
                allies_project=None
            
            try:
                projects= AllieProject.objects.filter(allie=allies_project)
                investigation_projects=[]
                for p in projects:
                    investigation_projects.append(p.investigation_project)
            except AllieProject.DoesNotExist:
                investigation_projects=[]
                
        allies= Allie.objects.all()

        return render(request, 'investigation_projects.html', {'investigation_projects': investigation_projects, 'allies': allies})
    