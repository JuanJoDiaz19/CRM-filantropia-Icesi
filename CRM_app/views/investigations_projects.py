from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from CRM_app.models import Investigation_Project

class InvestigationsProjects(View):
    def get(self, request):
        investigation_projects = Investigation_Project.objects.all()  # Obtener todas las instancias de investiagation_projecs
        return render(request, 'investigation_projects.html', {'investigation_projects': investigation_projects}) 