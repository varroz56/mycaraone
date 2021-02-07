from django.test import TestCase, Client
from django.shortcuts import get_object_or_404
from django.urls import reverse

from home.models import ContactUsMessage

from home.views import IndexView, ContactFormView


class TestIndexView(TestCase):
    """ Test the index view """

    def test_index_view(self):
        client = Client()

        response = client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')


class TestContactFormView(TestCase):
    """ test contact form view views """

    def setUp(self):
        """ initial test vars """
        self.client = Client()
        self.index_url = reverse('index')
        self.contact_us_message_url = reverse('contact_us_message')
        ContactUsMessage.objects.create(
            name='test name',
            email='test@email.com',
            subject='test subject',
            message='test message'
        )

    def test_contactform_view(self):
        client = Client()
        response = client.get(reverse('contact_us_message'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_contactusform_submitted(self):
        response = self.client.post(self.contact_us_message_url, {
            'name': 'test name post',
            'email': 'test@email.compost',
            'subject': 'test subject post',
            'message': 'test message post'

        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(get_object_or_404(ContactUsMessage,
                                           name='test name post').message, 'test message post')
