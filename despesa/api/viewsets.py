from rest_framework import viewsets
from despesa.api import serializers
from despesa import models

class DespesaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DespesaSerializer
    queryset = models.Despesa.objects.all()