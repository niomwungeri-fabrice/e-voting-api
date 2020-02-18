from unittest import TestCase
from tests.factories import AccountFactory
from rest_framework.test import APIClient


class BaseTest(TestCase):
    def setUp(self):
        self.user = AccountFactory()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
