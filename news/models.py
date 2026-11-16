
from django.db import models

class loading(models.Model):

    Roll_number = models.CharField(max_length=20, unique=True)

    name = models.CharField(max_length=100)

    division = models.CharField(max_length=10)

    def __str__(self):
        return self.name
