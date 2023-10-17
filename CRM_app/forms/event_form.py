from django.forms import ModelForm
from CRM_app.models import Event

class create_event_form(ModelForm):
    class Meta:
        model= Event
        fields= ['event_type_id','date', 'name','objective','description']