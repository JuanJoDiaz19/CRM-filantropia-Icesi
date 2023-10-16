from django.test import TestCase
from CRM_app.models import Event, Event_Type, EventAllie
from django.shortcuts import get_object_or_404
import datetime
import os
import base64

class ProductModelEvent(TestCase):
    def test_creation_event(self):
        event1 = Event_Type.objects.create(id=1, name="Nombre del Tipo de Evento")
        
        event = Event.objects.create(
                event_type_id= event1,
                date= "2021-02-04",
                name="ayuda a los pobres",
                objective="que mas",
                description= "pues bebe",
            
            )
        
        self.assertEqual(event.name, "ayuda a los pobres")
        self.assertEqual(event.date, "2021-02-04") 