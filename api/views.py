from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .serializers import DepartamentoSerializer
from cto.models import Departamento, Partes

from django.db.models import Q

class DepartamentoList(APIView):
    def get(self,request):
        depa = Departamento.objects.all()
        data = DepartamentoSerializer(depa,many=True).data
        return Response(data)


class DepartamentoDetalle(APIView):
    def get(self,request, claveDepartamento):
        depa = get_object_or_404(Departamento,Q(claveDepartamento=claveDepartamento))
        data = DepartamentoSerializer(depa).data
        return Response(data)


class PartesList(APIView):
    def get(self,request):
        func = Partes.objects.all()
        data = PartesSerializer(func,many=True).data
        return Response(data)


class PartesDetalle(APIView):
    def get(self,request, codigo):
        func = get_object_or_404(Partes,Q(codigo=codigo))
        data = PartesSerializer(func).data
        return Response(data)


