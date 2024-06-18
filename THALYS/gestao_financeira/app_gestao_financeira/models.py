from django.db import models

class Usuario(models.Model):
    id_receita = models.AutoField(primary_key=True)
    receita = models.TextField(max_length=225)
    gasto = models.FloatField()
