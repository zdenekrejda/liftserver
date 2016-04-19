from django.db import models
from django.utils import timezone

class Module(models.Model):
    module_id = models.CharField(max_length=64, unique=True)
    created_on = models.DateTimeField(
            default=timezone.now)
    connected = models.BooleanField(default=False)

    def publish(self):
        self.created_on = timezone.now()
        self.connected = False
        self.save()

    def connected(self):
        self.connected = True
        self.save()

    def __str__(self):
        return self.module_id
