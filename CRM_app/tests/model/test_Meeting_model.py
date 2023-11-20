from django.test import TestCase
from CRM_app.models import Meeting, Meeting_type, Allie, Allie_Type
from django.shortcuts import get_object_or_404

class ProductModelMeeting(TestCase):
    def test_creation_Meeting(self):
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
        
        
        meet= Meeting.objects.create(
            allie_id=ally,
            meeting_type_id=meeting1,
            date="2011-09-30",
            title="Filosofando sobre los filosofos"
        )

        self.assertEqual(meet.title,"Filosofando sobre los filosofos" )
        self.assertEqual(meet.date,"2011-09-30")