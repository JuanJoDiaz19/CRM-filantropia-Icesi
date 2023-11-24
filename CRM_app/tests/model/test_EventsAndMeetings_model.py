from django.test import TestCase
from django.urls import reverse
from CRM_app.models import Allie, Allie_Type, Event, Event_Type, Gender, Meeting, Meeting_type

class TestEventsAndMeetingsView(TestCase):
    def setUp(self):
        self.allie_type = Allie_Type.objects.create(name="Tipo de Aliado")
        self.allie = Allie.objects.create(name="Ejemplo Aliado", allie_type_id=self.allie_type)
        self.event_type = Event_Type.objects.create(name="Florescimiento")
        self.meeting_type = Meeting_type.objects.create(name="Tipo 1")
        self.event = Event.objects.create(name="Evento de Ejemplo", description="Descripción del evento", date="2023-10-10", event_type_id=self.event_type)
        self.meeting = Meeting.objects.create(title="Reunión de Ejemplo", description="Descripción de la reunión", allie=self.allie, date="2023-10-10",meeting_type_id=self.meeting_type)

    def test_events_and_meetings_view(self):
        url = reverse('events_and_meetings')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Evento de Ejemplo")
        self.assertContains(response, "Reunión de Ejemplo")