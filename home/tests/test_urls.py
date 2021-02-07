from django.test import SimpleTestCase
from django.urls import reverse, resolve

from home.views import IndexView, ContactFormView


class TestHomeUrls(SimpleTestCase):
    """ Test home urls """

    def test_to_fail(self):
        # check test to fail
        self.assertEqual(1, 2)

    def test_to_pass(self):
        # check test to pass
        self.assertEqual(1, 1)

    def test_index_url_is_resolved(self):
        # index
        url = reverse('index')
        self.assertEqual(resolve(url).func, IndexView)

    def test_contactusmessage_is_resolved(self):
        # contact us message
        url = reverse('contact_us_message')
        self.assertEqual(resolve(url).func, ContactFormView)
