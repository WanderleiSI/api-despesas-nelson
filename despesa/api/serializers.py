from rest_framework import serializers
from despesa import models

class DespesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Despesa
        fields = '__all__'