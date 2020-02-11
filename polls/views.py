from rest_framework import permissions, viewsets
from polls.models import Poll
from polls.serializers import PollSerializer


class CreatePollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(created_by=user)
