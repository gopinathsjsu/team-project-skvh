from django.db import models
import datetime

# Create your models here.
class Instructor(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True, unique=True)

    def __str__(self):
        return self.name