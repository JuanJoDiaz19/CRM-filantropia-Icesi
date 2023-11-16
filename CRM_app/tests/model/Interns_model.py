from django.test import TestCase
from django.urls import reverse
from CRM_app.models import Allie_Type, Practicing, Allie, Career, Gender

class TestInternsView(TestCase):
    def setUp(self):
        self.career = Career.objects.create(name="Carrera de Ejemplo")
        self.allie_type = Allie_Type.objects.create(name="Tipo de Aliado")
        self.allie = Allie.objects.create(name="Ejemplo Aliado", allie_type_id=self.allie_type)
        self.gender = Gender.objects.create(name="Masculino")

        self.intern1 = Practicing.objects.create(id=1,name="Practicante 1", allie_id=self.allie, career_id=self.career, gender_id=self.gender)
        self.intern2 = Practicing.objects.create(id=2,name="Practicante 2", allie_id=self.allie, career_id=self.career, gender_id=self.gender)

    def test_interns_view(self):
        url = reverse('interns', kwargs={'allie__id': self.allie.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Practicante 1")
        self.assertContains(response, "Practicante 2")

    def test_interns_view_with_query(self):
        url = reverse('interns', kwargs={'allie__id': self.allie.id})
        response = self.client.get(url, {'q': 'Practicante 1'})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Practicante 1")
        self.assertNotContains(response, "Practicante 2")

    def test_interns_view_with_invalid_allie_id(self):
        url = reverse('interns', kwargs={'allie__id': 999})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "")

    def test_interns_view_with_empty_query(self):
        url = reverse('interns', kwargs={'allie__id': self.allie.id})
        response = self.client.get(url, {'q': ''})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Practicante 1")
        self.assertContains(response, "Practicante 2")
        
