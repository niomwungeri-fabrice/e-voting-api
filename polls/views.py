from rest_framework import permissions, generics

from polls.models import Poll
from polls.serializers import PollSerializer


class CreatePollView(generics.CreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = (permissions.IsAdminUser,)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(created_by=user)


class PollListView(generics.CreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = (permissions.IsAdminUser,)


class PollUpdateRetrieveDestroyView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
