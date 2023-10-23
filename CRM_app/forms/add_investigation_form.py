from django.forms import ModelForm
from CRM_app.models import Investigation_Project

class create_invest_form(ModelForm):
    class Meta:
        model=Investigation_Project
        fields= ['name','description','active','start_date']