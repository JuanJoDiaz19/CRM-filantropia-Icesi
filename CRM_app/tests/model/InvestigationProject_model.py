from django.test import TestCase
from django.urls import reverse
from CRM_app.models import Investigation_Project

class TestResearchProjectView(TestCase):
    def setUp(self):
        self.project = Investigation_Project.objects.create(
            name="Proyecto de Investigación Ejemplo",
            description="Descripción del proyecto",
            start_date="2023-10-10"
        )

    def test_investigation_project_view(self):
        url = reverse('single_page_investigation_projects', kwargs={'project__id': self.project.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Proyecto de Investigación Ejemplo")
        self.assertContains(response, "Descripción del proyecto")
