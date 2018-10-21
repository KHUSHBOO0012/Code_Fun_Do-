from django.db import models

# Create your models here.
class State(models.Model):
    rainfall = models.CharField(max_length=10)
    warning = models.TextField(max_length=1000)


