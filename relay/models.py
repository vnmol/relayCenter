from django.db import models
from django.utils.timezone import now


class Enterprise(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Port(models.Model):
    PROTOCOL = (('UDP', 'UDP'), ('TCP', 'TCP'),)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    protocol = models.CharField(max_length=7, choices=PROTOCOL, default='TCP')
    ports = models.TextField()
    begin = models.DateTimeField(default=now)
    end = models.DateTimeField(blank=True, null=True)
