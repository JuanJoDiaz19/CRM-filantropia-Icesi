from django.shortcuts import render, redirect
from django.views import View

class Tasks(View):
    def get(self, request):
        return render(request, 'tasks.html')