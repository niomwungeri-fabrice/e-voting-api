from rest_framework import serializers

from polls.models import Poll


class PollSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Poll
        fields = "__all__"
