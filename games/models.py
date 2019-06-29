from django.db import models
from django.contrib.postgres.fields import JSONField


class GameSession(models.Model):
    game = models.CharField(max_length=20, null=False, blank=False)
    state = JSONField(default=dict, null=True, blank=False)
    started_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



