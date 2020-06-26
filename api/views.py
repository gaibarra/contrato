from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .serializers import DepartamentoSerializer
from cto.models import Departamento

from django.db.models import Q

class DepartamentoList(APIView):
    def get(self,request):
        depa = Departamento.objects.all()
        data = DepartamentoSerializer(depa,many=True).data
        return Response(data)


class DepartamentoDetalle(APIView):
    def get(self,request, clavedepto):
        depa = get_object_or_404(Departamento,Q(clavedepto=clavedepto))
        data = DepartamentoSerializer(depa).data
        return Response(data)





