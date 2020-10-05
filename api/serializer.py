from rest_framework import serializers

from cto.models import Contratos


class ContratosSerializer(serializers.ModelSerializer):

    class Meta:
        model=Contratos
        fields='__all__'

   