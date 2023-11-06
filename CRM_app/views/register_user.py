from django.shortcuts import render, redirect
from django.views import View
from CRM_app.forms.custom_user_form import CustomUserCreationForm

class RegisterUser(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(request.POST['password'])
            user.save()
            return redirect('login')
        return render(request, 'register.html', {'form': form})
