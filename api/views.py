from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from api.serializer import ContratosSerializer
from cto.models import Contratos

from django.db.models import Q

class ContratosList(APIView):
    def get(self,request):
        cont = Contratos.objects.all()
        data =ContratosSerializer(cont,many=True).data
        return Response(data)


class ContratosDetalle(APIView):
    def get(self,request, id):
        cont = get_object_or_404(Contratos,Q(id=id))
        data = ContratosSerializer(cont).data
        return Response(data)


