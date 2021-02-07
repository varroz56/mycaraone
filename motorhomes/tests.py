from django.test import TestCase, Client, SimpleTestCase
from django.urls import reverse, resolve


from .views import MotorhomeListView


class TestMotorhomeViews(TestCase):
    """ Test the index view """

    def setUp(self):
        """ initial test vars """
        self.client = Client()
        self.motorhomes_url = reverse('motorhomes')
        # self.motorhome_details_url = reverse(
        #     'motorhome_details', kwargs={pk: 1})

    def test_motorhomes_view(self):
        client = Client()
        response = client.get(reverse(MotorhomeListView))
        self.assertEqual(response.status_code, 200)


class TestMotorhomessUrls(SimpleTestCase):
    """ Test Motorhome urls """

    def test_to_fail(self):
        # check test to fail
        self.assertEqual(1, 2)

    def test_to_pass(self):
        # check test to pass
        self.assertEqual(1, 1)

    def test_MotorhomeListView_url_is_resolved(self):

        url = reverse('motorhomes')
        self.assertEqual(resolve(url).func, MotorhomeListView)
