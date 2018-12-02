from django.db import models

# Create your models here.
class AccountPurse(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)
    owner = models.CharField()
    amount_cp = models.IntegerField("cp")
    amount_sp = models.IntegerField("sp")
    amount_ep = models.IntegerField("ep")
    amount_gp = models.IntegerField("gp")
    amount_pp = models.IntegerField("pp")