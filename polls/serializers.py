from rest_framework import serializers
from accounts import serializers as user_serializer
from polls.models import Poll


class PollSerializer(serializers.ModelSerializer):
    created_by = user_serializer.UserSerializer(partial=True, required=False)

    class Meta:
        model = Poll
        fields = ['id', 'name', 'created_on', 'created_by']
