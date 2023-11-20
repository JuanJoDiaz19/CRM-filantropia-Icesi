from django.test import TestCase
from CRM_app.models import Allie, ContactInfo, Allie_Type, Area
from CRM_app.views import add_contact
from django.urls import reverse
from django.contrib.auth.models import User

class ContactInfoModelTest(TestCase):
    def setUp(self):
        self.allie_type = Allie_Type.objects.create(id=1, name="Tipo de prueba")
        self.area = Area.objects.create(id=1, area_description="Área de prueba")
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.allie = Allie.objects.create(
            allie_type_id=self.allie_type,
            name="Nombre de prueba",
            area_id=self.area,
            active=True,
            image_link="URL de la imagen de prueba",
            description="Descripción de prueba",
        )

    def test_crear_contacto(self):
        contact_info = ContactInfo.objects.create(
            id="contact_id_1",
            allie=self.allie,
            email="contacto@example.com",
            phone_number="1234567890",
            aux_email="aux_contacto@example.com",
            name="Nombre de contacto",
        )

        self.assertEqual(ContactInfo.objects.count(), 1)
        self.assertEqual(contact_info.name, "Nombre de contacto")
        self.assertEqual(contact_info.allie, self.allie)

class AddContactViewTest(TestCase):
    def setUp(self):
        self.allie_type = Allie_Type.objects.create(id=1, name="Tipo de prueba")
        self.area = Area.objects.create(id=1, area_description="Área de prueba")
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.allie = Allie.objects.create(
            allie_type_id=self.allie_type,
            name="Nombre de prueba",
            area_id=self.area,
            active=True,
            image_link="URL de la imagen de prueba",
            description="Descripción de prueba",
        )

    def test_agregar_contacto(self):
        self.client.login(username='testuser', password='testpassword')
        contact_data = {
            'contact_name': 'Nuevo Contacto',
            'contact_document_id': 'contact_id_2',
            'contact_phone': '9876543210',
            'contact_email': 'nuevo_contacto@example.com',
            'contact_aux_email': 'aux_nuevo_contacto@example.com',
        }
        response = self.client.post(reverse('add_contact', args=[self.allie.id]), data=contact_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ContactInfo.objects.count(), 1)
        new_contact = ContactInfo.objects.first()
        self.assertEqual(new_contact.name, 'Nuevo Contacto')
        self.assertEqual(new_contact.allie, self.allie)
