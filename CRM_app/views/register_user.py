from django.shortcuts import render, redirect
from django.views import View
from CRM_app.forms.custom_user_form import CustomUserCreationForm
from CRM_app.models import User_Type
import base64
import os

class RegisterUser(View):
    def get(self, request):
        form = CustomUserCreationForm()
        user_type= User_Type.objects.all()
        return render(request, 'register.html', {'form': form, 'users': user_type})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(request.POST['password'])
            user.user_type_id = form.cleaned_data['user_type_id']
            default_image_path = os.path.join('CRM_app/static/img/home/', 'profile.png')
            with open(default_image_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

            user.image_link = encoded_string
            user.save()
            return redirect('login')
        return render(request, 'register.html', {'form': form})
