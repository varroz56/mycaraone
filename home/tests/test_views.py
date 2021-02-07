from django.test import TestCase, Client
from django.shortcuts import get_object_or_404
from django.urls import reverse

from home.models import ContactUsMessage


class TestIndexView(TestCase):
    """ Test the index view """

    def setUp(self):
        """ initial test vars """
        self.client = Client()
        self.index_url = reverse('index')

    def test_index_view(self):
        client = Client()

        response = client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_contactusform_submitted(self):
        response = self.client.post(self.index_url, {
            'name': 'test name post',
            'email': 'test@email.compost',
            'subject': 'test subject post',
            'message': 'test message post'

        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(get_object_or_404(ContactUsMessage,
                                           name='test name post').message, 'test message post')

    def test_contactusform_ref_created(self):
        response = self.client.post(self.index_url, {
            'name': 'test name post',
            'email': 'test@email.compost',
            'subject': 'test subject post',
            'message': 'test message post'

        })
        if response.status_code == 200:
            self.assertEqual(get_object_or_404(ContactUsMessage,
                                               name='test name post').reference, 'CMF0000001')
