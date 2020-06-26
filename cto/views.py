from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required, permission_required

from .models import Departamento
from .forms import DepartamentoForm

from bases.views import SinPrivilegios



class VistaBaseCreate(SuccessMessageMixin,SinPrivilegios,generic.CreateView):
    context_object_name = 'obj'
    success_message="Registro Agregado Satisfactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)



# Vista generica para actualizar registros


class VistaBaseEdit(SuccessMessageMixin,SinPrivilegios, generic.UpdateView):
    context_object_name = 'obj'
    success_message="Registro Actualizado Satisfactoriamente"

    def form_valid(self, form):
        #form.instance.um = self.request.user.id
        return super().form_valid(form)




class DepartamentoView(SinPrivilegios,generic.ListView):
        model = Departamento
        template_name = "cto:departamento_list.html"
        context_object_name = "obj"
        permission_required = "cto.view_departamento"


class DepartamentoNew(VistaBaseCreate):
    model=Departamento
    template_name="cto/departamento_form.html"
    form_class=DepartamentoForm
    success_url= reverse_lazy("cto:departamento_list")
    permission_required="cto.add_departamento" 

class DepartamentoEdit(VistaBaseEdit):
    model = Departamento
    template_name="cto/departamento_form.html"
    form_class = DepartamentoForm
    success_url= reverse_lazy("cto:departamento_list")
    permission_required="cto.change_departamento"


@login_required(login_url="/login/")
@permission_required("cto.change_departamento",login_url="/login/")
def departamentoInactivar(request,id):
    departamento = Departamento.objects.filter(pk=id).first()

    if request.method=="POST":
        if departamento:
            departamento.estado = not departamento.estado
            departamento.save()
            return HttpResponse("OK")
        return HttpResponse("FAIL")
    
    return HttpResponse("FAIL")          

