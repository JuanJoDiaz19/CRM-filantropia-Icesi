from django.shortcuts import render, redirect
from django.views import View
from CRM_app.forms.NewForm import NewForm

class allies(View):
    
    def get(self,request):
        return render(request,"allies.html")