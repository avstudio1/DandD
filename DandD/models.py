from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

class PerformanceModel(models.Model):
    date = models.DateField()
    total_flights = models.IntegerField()
    total_blocks = models.IntegerField()
    total_SLA = models.IntegerField()
    missed_flights = models.IntegerField()
    percent_blocks = models.FloatField()
    percent_SLA = models.FloatField()
    
