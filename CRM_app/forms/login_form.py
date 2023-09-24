from django import forms
from CRM_app.models.New import New

class NewForm(forms.ModelForm):
    class Meta:
        model = New
        fields = ['name', 'password']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }
