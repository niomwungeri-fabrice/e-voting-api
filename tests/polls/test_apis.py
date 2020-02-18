from rest_framework import status

from tests.set_up import BaseTest


class PollPrivateAPITests(BaseTest):

    def test_create_poll_successfully(self):
        res = self.client.post('/api/v1/polls/create/', {
            'name': "body1038",
        })
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['name'], 'body1038')
