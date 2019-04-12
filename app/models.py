from django.db import models

# Create your models here.


class StarWars(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    image = models.URLField(max_length=250, null=True, blank=True)

    class Meta:
        db_table = 'starwars'

