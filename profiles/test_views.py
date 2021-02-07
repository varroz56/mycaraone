from django.test import TestCase, Client
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import UserProfile

from .views import UserProfileView, UserProfileUpdateView, CreateBillingAddressView, UpadeBillingAddressView, DeleteBillingAddressView, ConfirmDeleteBillingAddressView
from checkout.models import BillingAddress


class TestProfilesView(TestCase):
    """ Test the index view """

    def setUp(self):
        """ initial test vars """
        self.client = Client()
        self.myprofile_url = reverse('myprofile')
        self.update_myprofile_url = reverse('update_myprofile')
        self.create_billing_address_url = reverse('create_billing_address')
        self.update_billing_address_url = reverse('update_billing_address')
        self.confirm_delete_billing_address_url = reverse(
            'confirm_delete_billing_address')
        self.delete_billing_address_url = reverse('delete_billing_address')

    def test_myprofile_view(self):
        client = Client()
        response = client.get(reverse(UserProfileView))
        self.assertEqual(response.status_code, 302)

    def test_update_myprofile_view(self):
        self.client = Client()
        response = self.client.post(reverse(UserProfileUpdateView))
        self.assertEqual(response.status_code, 302)

    def test_create_billing_address_view(self):
        self.client = Client()
        response = self.client.post(reverse(CreateBillingAddressView))
        self.assertEqual(response.status_code, 302)

    def test_update_billing_address_view(self):
        self.client = Client()
        response = self.client.post(reverse(UpadeBillingAddressView))
        self.assertEqual(response.status_code, 302)

    def test_confirm_delete_billing_address_view(self):
        client = Client()
        response = client.get(reverse(ConfirmDeleteBillingAddressView))
        self.assertEqual(response.status_code, 302)

    def test_delete_billing_address_view(self):
        client = Client()
        response = client.get(reverse(DeleteBillingAddressView))
        self.assertEqual(response.status_code, 302)
