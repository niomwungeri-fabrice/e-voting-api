from rest_framework import status
from rest_framework.test import APIClient

from tests.set_up import BaseTest


class MyTestCase(BaseTest):

    def setUp(self):
        self.client = APIClient()

    def test_unauthorized_user_fetching(self):
        res = self.client.get('/users/')
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(res.data['detail'],
                         'Authentication credentials were not provided.')
