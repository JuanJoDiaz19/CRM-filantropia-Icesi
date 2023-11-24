from django.test import TestCase
from CRM_app.forms import event_form
from CRM_app.models import Event_Type


class FormsTestCase(TestCase):
  def test_valid_event_form(self):
      event_type = Event_Type.objects.create(id=1, name="Tipo de Evento Ejemplo")
      data = { 
            'event_type_id':event_type,
            'date':'2023-02-04',
            'name':'Mateo',
            'objective':'que mas',
            'description': 'pues bebe',
            
        }
      
      form=event_form.create_event_form(data=data)
      
      self.assertTrue(form.is_valid())