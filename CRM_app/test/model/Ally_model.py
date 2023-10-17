from django.test import TestCase
from CRM_app.models import Allie, Allie_Type, Area

class AllieModelTest(TestCase):
    def setUp(self):
        self.allie_type = Allie_Type.objects.create(id=1, name="Tipo de prueba")
        self.area = Area.objects.create(id=1, area_description="Área de prueba")

    def test_crear_allie(self):
        ally = Allie.objects.create(
            allie_type_id=self.allie_type,
            name="Nombre de prueba",
            area_id=self.area,
            active=True,
            image_link="URL de la imagen de prueba",
            description="Descripción de prueba",
        )

        self.assertEqual(Allie.objects.count(), 1)
        self.assertEqual(ally.name, "Nombre de prueba")
        self.assertTrue(ally.active)
        self.assertEqual(ally.image_link, "URL de la imagen de prueba")
        self.assertEqual(ally.description, "Descripción de prueba")
        self.assertEqual(ally.allie_type_id, self.allie_type)
        self.assertEqual(ally.area_id, self.area)

    def test_crear_allie_sin_descripcion(self):
      ally = Allie.objects.create(
          allie_type_id=self.allie_type,
          name="Nombre de prueba",
          area_id=self.area,
          active=True,
          image_link="URL de la imagen de prueba",
      )

      self.assertEqual(Allie.objects.count(), 1)
      self.assertIsNone(ally.description)

    def test_crear_allie_sin_imagen(self):
        ally = Allie.objects.create(
            allie_type_id=self.allie_type,
            name="Nombre de prueba",
            area_id=self.area,
            active=True,
        )

        self.assertEqual(Allie.objects.count(), 1)
        self.assertEqual(ally.image_link, "")
