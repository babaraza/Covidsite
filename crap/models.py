from django.db import models


class CovidData(models.Model):
    total_deaths = models.CharField(max_length=20)
    total_infections = models.CharField(max_length=20)
    last_updated = models.CharField(max_length=20)

    def __str__(self):
        return f'☠️ {self.total_deaths}'
