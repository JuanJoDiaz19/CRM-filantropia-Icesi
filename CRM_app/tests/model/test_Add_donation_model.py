from django.test import TestCase
from CRM_app.forms import donation_form
from CRM_app.models import Allie, Allie_Type, Donation_Type, Donation

class DonationsTestCase(TestCase):
    def test_valid_donation_model(self):

        allie_type= Allie_Type.objects.create(id=1, name="eo")
        ally= Allie.objects.create(
            allie_type_id= allie_type,
            name="Santiago",
            area="b*h",
            active=True,
            image_link="aaa",
            description="dejate ver, dime si hoy vas pa la calle bebé",
        )
        donation = Donation_Type.objects.create(id=1, max_value=5, min_value=1, name='hola')
        donation2 = Donation.objects.create(id= 1,
            date= '2023-10-15',
            amount= 3,
            donation_type_id= donation,
            allie_id= ally,
            description= 'se iban')
        
        
        self.assertEqual(donation2.amount, 3)
        self.assertEqual(donation2.allie_id, ally)
        