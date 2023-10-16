from django.test import TestCase
from CRM_app.forms import meet_form
from CRM_app.models import Meeting_type, Allie, Allie_Type

class FormsTestCase(TestCase):
    def test_valid_meeting_form(self):
        allie_type= Allie_Type.objects.create(id=1, name="Wao")
        ally= Allie.objects.create(
            allie_type_id= allie_type,
            name="Mateo",
            area="Especialista en Qa",
            active=True,
            image_link="aaa",
            description="que mas pues bebe, sigo aqui pensando en ti otra vez",
        )
        meeting1= Meeting_type.objects.create(id=1, name="Nombre de la reunion")
        data={
            'allie_id':ally,
            'meeting_type_id': meeting1,
            'date': '2023-10-15',
            'title': 'Sembremos'
        }
        
        form= meet_form.create_meeting_form(data=data)
        
        self.assertTrue(form.is_valid())
        
        

