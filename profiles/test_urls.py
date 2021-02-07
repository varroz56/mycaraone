from django.test import SimpleTestCase
from django.urls import reverse, resolve

from profiles.views import UserProfileView, UserProfileUpdateView, CreateBillingAddressView, UpadeBillingAddressView, ConfirmDeleteBillingAddressView, DeleteBillingAddressView


class TestProfilesUrls(SimpleTestCase):
    """ Test home urls """

    def test_to_fail(self):
        # check test to fail
        self.assertEqual(1, 2)

    def test_to_pass(self):
        # check test to pass
        self.assertEqual(1, 1)

    def test_UserProfileView_url_is_resolved(self):

        url = reverse('myprofile')
        self.assertEqual(resolve(url).func, UserProfileView)

    def test_UserProfileUpdateView_url_is_resolved(self):

        url = reverse('update_myprofile')
        self.assertEqual(resolve(url).func, UserProfileUpdateView)

    def test_CreateBillingAddressView_url_is_resolved(self):

        url = reverse('create_billing_address')
        self.assertEqual(resolve(url).func, CreateBillingAddressView)

    def test_UpadeBillingAddressView_url_is_resolved(self):

        url = reverse('update_billing_address')
        self.assertEqual(resolve(url).func, UpadeBillingAddressView)

    def test_ConfirmDeleteBillingAddressView_url_is_resolved(self):

        url = reverse('confirm_delete_billing_address')
        self.assertEqual(resolve(url).func, ConfirmDeleteBillingAddressView)

    def test_DeleteBillingAddressView_url_is_resolved(self):

        url = reverse('delete_billing_address')
        self.assertEqual(resolve(url).func, DeleteBillingAddressView)
