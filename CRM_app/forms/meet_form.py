from django.forms import ModelForm
from CRM_app.models import Meeting

class create_meeting_form(ModelForm):
    class Meta:
        model= Meeting
        fields= ['allie_id','meeting_type_id','date','title']