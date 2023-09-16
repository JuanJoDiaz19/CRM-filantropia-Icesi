from django import forms
from .models import New

class NewForm(forms.ModelForm):
    class Meta:
        model = New
        fields = ['title', 'description', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }

