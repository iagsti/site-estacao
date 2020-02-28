from django.db import models
from estacao.core.managers import ConditionsManager


class Dados(models.Model):
    data = models.DateTimeField('Data', primary_key=True)
    vis = models.IntegerField('Vis')
    tipob = models.CharField(max_length=12)
    qtdb = models.IntegerField()
    tipom = models.CharField(max_length=12)
    qtdm = models.IntegerField()
    tipoa = models.CharField(max_length=12)
    qtda = models.IntegerField()
    dir = models.CharField(max_length=12)
    vento = models.FloatField()
    temp_bar = models.FloatField()
    pressao = models.FloatField()
    tseco = models.FloatField()
    tumido = models.FloatField()
    tsfc = models.FloatField()
    t5cm = models.FloatField()
    t10cm = models.FloatField()
    t20cm = models.FloatField()
    t30cm = models.FloatField()
    t40cm = models.FloatField()
    piche = models.FloatField()
    evap_piche = models.FloatField()
    piche_ar = models.FloatField()
    evap_piche_ar = models.FloatField()
    tmax = models.FloatField()
    tmin = models.FloatField()

    class Meta:
        managed = False
        db_table = 'dados'

    objects = ConditionsManager()