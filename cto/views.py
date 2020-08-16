from django.shortcuts import render,redirect, get_list_or_404
from django.views import generic 
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User               
from django.http import HttpResponse
from datetime import datetime, date
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate
from bases.views import SinPrivilegios
from bases.views import *
from .models import Departamento, Partes, Contratos, Doctos, Tipocontrato, Requisitos
from .forms import DepartamentoForm, PartesForm, ContratosForm
from bases.views import SinPrivilegios
from django.core.files.storage import FileSystemStorage









class VistaBaseCreate(SuccessMessageMixin,SinPrivilegios,generic.CreateView):
    context_object_name = 'obj'
    success_message="Registro Agregado Satisfactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)




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

class PartesView(SinPrivilegios,generic.ListView):
        model = Partes
        template_name = "cto:partes_list.html"
        context_object_name = "obj"
        permission_required = "cto.view_partes"


class PartesNew(VistaBaseCreate):
    model= Partes
    template_name="cto/partes_form.html"
    form_class=PartesForm
    success_url= reverse_lazy("cto:partes_list")
    permission_required="cto.add_departamento" 

class PartesEdit(VistaBaseEdit):
    model = Partes
    template_name="cto/partes_form.html"
    form_class = PartesForm
    success_url= reverse_lazy("cto:partes_list")
    permission_required="cto.change_partes"


@login_required(login_url="/login/")
@permission_required("cto.change_partes",login_url="/login/")
def partesInactivar(request,id):
    partes = Partes.objects.filter(pk=id).first()

    if request.method=="POST":
        if partes:
            partes.estado = not partes.estado
            partes.save()
            return HttpResponse("OK")
        return HttpResponse("FAIL")
    
    return HttpResponse("FAIL")   
class ContratosView(SinPrivilegios, generic.ListView):
    model = Contratos
    template_name = "cto/contrato_list.html"
    context_object_name = "obj"
    success_url= reverse_lazy("cto:contrato_list")
    permission_required="cto.view_contratos"
        
    def get_queryset(self):
        
        current_userx = self.request.user.id
        #conditions = dict(current_user=current_userx, uc_id=self.request.user) 
        #queryset = queryset.filter(**conditions)
        return Contratos.objects.all()
        #return Contratos.objects.filter(
        #    Q(current_user=current_userx) | Q(uc_id=self.request.user)
        #)
        #return SpyorEnc.objects.filter(
        #    Q(current_user=current_userx) | Q(uc_id=self.request.user) | Q(el_jefe=current_userx)
        #)
        
    
    
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ContratosView, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['some_data'] = Partes.objects.all()
        context['some_data2'] = Departamento.objects.all()
        return context                   

@login_required(login_url='/login/')
@permission_required('cto.add_contratos', login_url='bases:sin_privilegios')
def contratos2(request,contrato_id=None):
    
    template_name='cto/contrato.html'
    detalle = {}
    secuencia_data = {}
    xUsuario = (request.user.id)
    print(xUsuario)
   
    partes = Partes.objects.filter(estado=True, user=xUsuario)    
    partes2 =Partes.objects.filter(estado=True)
    partes2 =Partes.objects.order_by('nombreParte')
    print (partes2)
    p=partes.first()
    print (p)
    
    
    d1 = p.claveDepartamento
    dx = p.claveDepartamento_id
    rfcparte = (p.rfc)
    print(rfcparte)
    
    print(d1)
   
    requisitos = Requisitos.objects.filter(estado=True)
    departamentos =Departamento.objects.filter(estado=True, claveDepartamento=dx)
    departamentos2 =Departamento.objects.filter(estado=True)
    d2=departamentos.first()
    d3= (d2.claveDepartamento)
    
    secuencia = (d2.f001)

    print (d3)
    print(secuencia)

    
    if secuencia:

        r1 = int(secuencia[:5])
        f1 = secuencia[5:8]
    
        r2 = int(secuencia[8:13])
        f2 = secuencia[13:16]
        
        if f1 == 'DIC':    
            funcionario =Partes.objects.filter( user_id=r1)
        else:
            funcionario =Partes.objects.filter( user_id=r2)
        
        print(funcionario)
        a2 = funcionario.first()
        print(a2)
        a3 = (a2.id )
        print (a3)
        fun=Partes.objects.get(pk=a3)
        r3 = int(secuencia[16:21])
        f3 = secuencia[21:24]
        
        r4 = int(secuencia[24:29])
        f4 = secuencia[29:32]
    
        r5 = int(secuencia[32:37])
        f5 = secuencia[37:40]
    
        r6 = int(secuencia[40:45])
        f6 = secuencia[45:48]

        print(r1)
        print(f1)
        print(r2)
        print(f2)
        print(r3)
        print(f3)
        print(r4)
        print(f4)
        print(r5)
        print(f5)
        print(r6)
        print(f6)
    else:
        print ("secuencia no asignada")    

    
    if request.method == "GET":
        enc = Contratos.objects.filter(pk=contrato_id).first()
        if not enc:
            encabezado = {
                'id':"",
                'uc_id':"",
                'tipocontrato':1,
                'datecontrato':datetime.today(),
                'datecontrato_ini':"",
                'datecontrato_fin':"",
                'parte1':546,
                'enCalidadDe1':"'CLIENTE '",
                'parte2':"",
                'enCalidadDe2':"'PRESTADOR DE SERVICIOS '",
                'lugarContrato':"",
                'ciudadContrato':"Mérida",
                'estadoContrato':"Yucatán",
                'paisContrato':"México",  
                'importeContrato':0.00,
                'npContrato':"",
                'imppContrato':0.00,
                'vhppContrato':285.00,
                'totalhorasContrato':"",
                'testigoContrato1':"",
                'testigoContrato2':"",
                'versionContrato':"",
        
                'status':"CAP",
                'rcap':xUsuario,
                
               
                'rstep1':r1,
                'rstep2':r2,
                'rstep3':r3,
                'rstep4':r4,
                'rstep5':r5,
                'rstep6':r6,
                
                
                'astep1':f1,
                'astep2':f2,
                'astep3':f3,
                'astep4':f4,
                'astep5':f5,
                'astep6':f6,
            
                'devuelto_por':"",

            
            }
            detalle=None
        else:
            
            encabezado = {
                'id':enc.id,
                'uc_id':enc.uc_id,
                'tipocontrato':enc.tipocontrato,
                'datecontrato':enc.datecontrato,
                'datecontrato_ini':enc.datecontrato_ini,
                'datecontrato_fin':enc.datecontrato_fin,
                'parte1':enc.parte1,
                'enCalidadDe1':enc.enCalidadDe1,
                'parte2':enc.parte2,
                'enCalidadDe2':enc.enCalidadDe2,
                'lugarContrato':enc.lugarContrato,
                'ciudadContrato':enc.ciudadContrato,
                'estadoContrato':enc.estadoContrato,
                'paisContrato':enc.paisContrato,  
                'importeContrato':enc.importeContrato,
                'npContrato':enc.npContrato,
                'imppContrato':enc.imppContrato,
                'vhppContrato':enc.vhppContrato,
                'totalhorasContrato':enc.totalhorasContrato,
                'testigoContrato1':enc.testigoContrato1,
                'testigoContrato2':enc.testigoContrato2,
                'versionContrato':enc.versionContrato,
        
                'status':enc.status,
                'rcap':enc.rcap,
                
               
                'rstep1':enc.rstep1,
                'rstep2':enc.rstep2,
                'rstep3':enc.rstep3,
                'rstep4':enc.rstep4,
                'rstep5':enc.rstep5,
                'rstep6':enc.rstep6,
                
                
                'astep1':enc.astep1,
                'astep2':enc.astep2,
                'astep3':enc.astep3,
                'astep4':enc.astep4,
                'astep5':enc.astep5,
                'astep6':enc.astep6,
            
                'devuelto_por':enc.devuelto_por,
                
                

            }

     
        
        detalle=Doctos.objects.filter(contrato=enc)
       
        contexto = {"requi":requisitos,"fun":funcionario,"fun2":partes2,"enc":encabezado,"det":detalle,"departamentos":departamentos,"funcionarios":partes,"departamentos2":departamentos2,}
        
        return render(request,template_name,contexto)
    
   
    
    if request.method == "POST":
        
        tipocontrato=1
        datecontrato  = request.POST.get("datecontrato")
        datecontrato_ini  = request.POST.get("enc_datecontrato_ini")
        datecontrato_fin  = request.POST.get("enc_datecontrato_fin")
        
        parte1 = 546
        parte2 = request.POST.get("enc_nombreParte")

        enCalidadDe1 = "'CLIENTE '"
        enCalidadDe2 = "'PRESTADOR DE SERVICIOS '"        
        
        lugarContrato = request.POST.get("lugarContrato")
        ciudadContrato = "Mérida"
        estadoContrato = "Yucatán"
        paisContrato = "México"
        importeContrato = request.POST.get("enc_importeContrato")
        npContrato = request.POST.get("enc_npContrato")
        imppContrato = request.POST.get("enc_imppContrato")
        vhppContrato = 285
        totalhorasContrato = request.POST.get("enc_totalhorasContrato")
        testigoContrato1 = request.POST.get("enc_testigoContrato1")
        testigoContrato2 = request.POST.get("enc_testigoContrato2")
        versionContrato = request.POST.get("versionContrato")
        status = request.POST.get("status")
       
        fun=Partes.objects.get(pk=a3)
        tip=Tipocontrato.objects.get(pk=1)
        
        if parte2:
         suj=Partes.objects.get(pk=parte2)
        

        if not contrato_id:
            enc = Contratos(
                tipocontrato = tip,
                datecontrato  = datecontrato,
                datecontrato_ini  = datecontrato_ini,
                datecontrato_fin  = datecontrato_fin,
                
                parte1 = parte1,
                parte2 = suj,
                ciudadContrato = ciudadContrato,
                estadoContrato = estadoContrato,
                paisContrato = paisContrato,
                              
                enCalidadDe1 = enCalidadDe1,
                enCalidadDe2 = enCalidadDe2,

                importeContrato = importeContrato,
                npContrato = npContrato,
                imppContrato = imppContrato,
                vhppContrato = vhppContrato,
                totalhorasContrato = totalhorasContrato,
                testigoContrato1 = testigoContrato1,
                testigoContrato2 = testigoContrato2,

                status = status,
                rcap = xUsuario,
                current_user = xUsuario,
                rstep1 = r1,
                rstep2 = r2,
                rstep3 = r3,
                rstep4 = r4,
                rstep5 = r5,
                rstep6 = r6,
                
                astep1 = f1,
                astep2 = f2,
                astep3 = f3,
                astep4 = f4,
                astep5 = f5,
                astep6 = f6,
                devuelto_por = False,
            )
            if enc:
                enc.save()
                contrato_id = enc.id
        else:
            enc = Contratos.objects.filter(pk=contrato_id).first()
            if enc:
                
                enc.funcionario = fun
                
                enc.save()
                
        if not id:
            messages.error(request,'No Puedo Continuar No Pude Detectar No. de Contrato')
            return redirect("cto:contrato_list")
        
        documento = request.POST.get("documento")
        comentarioDocto = request.POST.get("comentarioDocto")
        req = Requisitos.objects.get(pk=documento)
        vigenciaFinDocto = request.POST.get("enc_vigenciaFinDocto")
        
        pdf= request.POST.get('pdf2')
        
        uploaded_file = request.FILES['pdf']
        print(uploaded_file)
            
        fs = FileSystemStorage()
        print(fs)
        name = fs.save(uploaded_file.name, uploaded_file)
        print(name)
        pdf = name

        if vigenciaFinDocto != "":
        
            det = Doctos(
                contrato=enc,
                documento=req,
                comentarioDocto=comentarioDocto,
                pdf=pdf,
                vigenciaFinDocto=vigenciaFinDocto,
            
            )
        
        if vigenciaFinDocto == "":
            
            det = Doctos(
                contrato=enc,
                documento=req,
                comentarioDocto=comentarioDocto,
                pdf=pdf,
              
            
            )
        
        if det:
            det.save()
            
        
            return redirect("cto:contrato_edit",contrato_id=contrato_id)

    return render(request,template_name,contexto)

class ContratosEdit(VistaBaseEdit):
        model = Contratos
        template_name="cto/contrato_form.html"
        form_class = ContratosForm
        success_url= reverse_lazy('cto:contrato_list')
        permission_required="cto.change_contratos"
        context_object_name = 'obj'

         