from django.db import models
from django.utils.timezone import now
# Create your models here.
class Despesa(models.Model):
    descricao = models.TextField(max_length=100)
    categoria = models.IntegerField()
    valor = models.FloatField()
    data = models.DateField(default=now)
    user = models.IntegerField()

    def __str__(self):
        return self.descricao