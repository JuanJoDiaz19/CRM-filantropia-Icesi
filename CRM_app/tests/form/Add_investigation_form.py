from django.test import TestCase
from CRM_app.forms.add_investigation_form import create_invest_form  

class FormTestCase(TestCase):

    def test_investigation_project_form_with_invalid_data(self):
        
        form_data = {
            'name': '',
            'description': 'Descripción del proyecto de prueba',
            'active': True,
            'start_date': '2023-10-15',
        }

       
        form = create_invest_form(data=form_data)

        # Comprobar que el formulario es inválido debido al campo de nombre en blanco
        self.assertFalse(form.is_valid())