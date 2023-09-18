from django.shortcuts import render, redirect
from django.views import View
from CRM_app.forms.NewForm import NewForm

class CreateNew(View):
    def get(self, request):
        form = NewForm()  # Create an instance of the form
        return render(request, 'create_new.html', {'form': form})  # Render the form in the template

    def post(self, request):
        form = NewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
        return render(request, 'create_new.html', {'form': form})  # Render the form with errors

