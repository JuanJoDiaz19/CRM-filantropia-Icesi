from django.forms import ModelForm
from CRM_app.models import Donation

class add_donation_form(ModelForm):
    class Meta:
        model= Donation
        fields= ['id','date','amount','donation_type_id','allie_id','description']