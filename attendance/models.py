from django.db import models

class PunchRecord(models.Model):
    name = models.CharField(max_length=100)
    punched_at = models.DateTimeField(auto_now_add=True)
