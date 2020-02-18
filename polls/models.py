from django.db import models
import uuid
from accounts.models import User
from datetime import datetime


class Poll(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(default=datetime.now, blank=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
