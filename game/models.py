from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=300)
    url = models.URLField(max_length=300)
    Author = models.CharField(max_length=300)