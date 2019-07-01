from django.db import models
from django.utils import timezone


class report(models.Model):
    firstoccurrence = models.DateTimeField()
    node = models.CharField(max - legth=50)
    severity = models.CharField(max - legth=20)
    alarm = models.TextField()
