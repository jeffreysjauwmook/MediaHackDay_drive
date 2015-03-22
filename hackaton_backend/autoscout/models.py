from django.db import models

class trip_entry(models.Model):
    vim = models.CharField(max_length=200)
    timestamp = models.DateTimeField()
    km_total = models.IntegerField(default=0)
    km_diff = models.IntegerField(default=0)
    fuel_total = models.DecimalField(decimal_places=2, max_digits=99999)
    fuel_diff = models.DecimalField(decimal_places=2, max_digits=99999)
    heavy = models.BooleanField(default=False)
    checked = models.BooleanField(default=False)


