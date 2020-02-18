from polls.models import Poll
from tests.set_up import BaseTest


class TestPollModel(BaseTest):

    def test_create_poll(self):
        poll = Poll.objects.create(
            created_by=self.user,
            name="body1038",)
        self.assertEqual(str(poll), poll.name)
