from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=300)
    url = models.URLField(max_length=300)
    author = models.CharField(max_length=300)
    published_date = models.DateField()

    def __str__(self):
        return self.name