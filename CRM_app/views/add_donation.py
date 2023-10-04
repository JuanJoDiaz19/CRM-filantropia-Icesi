from django.shortcuts import render, redirect
from django.views import View
from CRM_app.models import Allie_Type, Allie, ContactInfo
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class AddDonation(View):
    def get(self, request):
        return render(request, 'allies/add-donation.html')
    