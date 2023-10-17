from django.test import TestCase
from CRM_app.models import Investigation_Project, Allie,AllieProject,Allie_Type
from django.shortcuts import get_object_or_404

class ProductModelInvestigation(TestCase):
    def test_create_investigation_project(self):
        
        # Crear un objeto de prueba para el modelo Investigation_Project
        project = Investigation_Project.objects.create(
            name="Proyecto de Prueba",
            description="Descripción del proyecto de prueba",
            active=True,
            start_date="2023-10-15",
            finish_date="2023-11-15"
        )

        # Comprobar que se creó el proyecto correctamente
        self.assertEqual(project.name, "Proyecto de Prueba")
        self.assertEqual(project.description, "Descripción del proyecto de prueba")
        self.assertTrue(project.active)
        self.assertEqual(project.start_date, "2023-10-15")
        self.assertEqual(project.finish_date, "2023-11-15")

    def test_create_allie(self):
        allie_type= Allie_Type.objects.create(id=1, name="Wao")
        # Crear un objeto de prueba para el modelo Allie
        allie = Allie.objects.create(
            allie_type_id=allie_type,  # Asumiendo que tienes un Allie_Type con ID 1
            name="Aliado de Prueba",
            area="Área de Prueba",
            active=True,
            image_link="ruta/a/imagen.jpg",
            description="Descripción del aliado de prueba"
        )

        # Comprobar que se creó el aliado correctamente
        self.assertEqual(allie.name, "Aliado de Prueba")
        self.assertEqual(allie.area, "Área de Prueba")
        self.assertTrue(allie.active)
        self.assertEqual(allie.image_link, "ruta/a/imagen.jpg")
        self.assertEqual(allie.description, "Descripción del aliado de prueba")

    def test_create_allie_project(self):
        allie_type= Allie_Type.objects.create(id=1, name="Wao")
        # Crear objetos de prueba para Allie y Investigation_Project
        allie = Allie.objects.create(
            allie_type_id=allie_type,
            name="Aliado de Prueba",
            area="Área de Prueba",
            active=True,
            image_link="ruta/a/imagen.jpg",
            description="Descripción del aliado de prueba"
        )
        project = Investigation_Project.objects.create(
            name="Proyecto de Prueba",
            description="Descripción del proyecto de prueba",
            active=True,
            start_date="2023-10-15",
            finish_date="2023-11-15"
        )

        # Crear un objeto de prueba para el modelo AllieProject
        allie_project = AllieProject.objects.create(
            investigation_project=project,
            allie=allie
        )

        # Comprobar que se creó la relación AllieProject correctamente
        self.assertEqual(allie_project.investigation_project, project)
        self.assertEqual(allie_project.allie, allie)
