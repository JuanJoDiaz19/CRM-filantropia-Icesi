from django.shortcuts import render, redirect
from django.views import View
from CRM_app.models import Donation,Allie

class InvestigationProject(View):
    def get(self, request):     
        return render(request, 'single_page_investigation_projects.html')