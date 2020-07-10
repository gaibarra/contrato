from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from datetime import datetime, date
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required, permission_required

from .models import Departamento, Partes, Contratos, Doctos
from .forms import DepartamentoForm, PartesForm

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
        return Contratos.objects.filter(
            Q(current_user=current_userx) | Q(uc_id=self.request.user)
        )
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
    
    template_name='cto/contratos.html'
    detalle = {}
    secuencia_data = {}
    xUsuario = (request.user.id)
    print(xUsuario)
    partes =Partes.objects.filter(estado=True)
    partes2 = Partes.objects.filter(estado=True, user=xUsuario)    
    p=partes2.first()
    d1 = p.clavedepto
    rfcparte = (p.rfc)
    print(rfcparte)
    print (p)
    print(d1)
   
   
    departamentos =Departamento.objects.filter(estado=True, clavedepto=d1)
    departamentos2 =Departamento.objects.filter(estado=True)
    d2=departamentos.first()
    d3= (d2.departamento)
    
    secuencia = (d2.f001)

    print (d3)
    print(secuencia)

    
    if secuencia:

        r1 = int(secuencia[:5])
        f1 = secuencia[5:8]
    
        r2 = int(secuencia[8:13])
        f2 = secuencia[13:16]
    
        if f1 == 'AUT':    
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
        enc = Contratos.objects.filter(pk=id).first()
        if not enc:
            encabezado = {
                'id':"",
                'uc_id':"",
                'tipocontrato':"",
                'datecontrato':" ",
                'datecontrato_ini':" ",
                'datecontrato_fin':" ",
                'parte1':"",
                'enCalidadDe1':"",
                'parte2':"",
                'enCalidadDe2':"",
                'lugarContrato':"",
                'ciudadContrato':"",
                'estadoContrato':"",
                'paisContrato':"",  
                'importeContrato':0.00,
                'npContrato':"",
                'imppContrato':0.00,
                'vhppContrato':0.00,
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
       
        contexto = {"fun2":partes2,"enc":encabezado,"det":detalle,"departamentos":departamentos,"funcionarios":partes,"departamentos2":departamentos2,}
        
        return render(request,template_name,contexto)
    
   
    
    if request.method == "POST":
        tipocontrato = request.POST.get("enc_beneficiario")
        datecontrato  = request.POST.get("datecontrato")
        datecontrato_ini  = request.POST.get("datecontrato_ini")
        datecontrato_fin  = request.POST.get("datecontrato_fin")
        parte1 = request.POST.get("parte1")
        enCalidadDe1 = request.POST.get("enCalidadDe1")
        parte2 = request.POST.get("parte2")
        enCalidadDe2 = request.POST.get("enCalidadDe2")
        lugarContrato = request.POST.get("lugarContrato")
        ciudadContrato = request.POST.get("ciudadContrato")
        estadoContrato = request.POST.get("estadoContrato")
        paisContrato = request.POST.get("paisContrato")
        importeContrato = request.POST.get("importeContrato")
        npContrato = request.POST.get("npContrato")
        imppContrato = request.POST.get("imppContrato")
        vhppContrato = request.POST.get("vhppContrato")
        totalhorasContrato = request.POST.get("totalhorasContrato")
        testigoContrato1 = request.POST.get("testigoContrato1")
        testigoContrato2 = request.POST.get("testigoContrato2")
        versionContrato = request.POST.get("versionContrato")
        status = request.POST.get("status")
       
        fun=Partes.objects.get(pk=a3)
        

        if not contrato_id:
            enc = Contratos(
                              
                
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
            messages.error(request,'No Puedo Continuar No Pude Detectar No. de Conrato')
            return redirect("cto:contrato_list")
        
        

        tipo_comprobante = request.POST.get("tipo_comprobante")
        no_facturasol = request.POST.get("no_facturasol")
        fecha_compra = request.POST.get("fecha_compra")
        importe = request.POST.get("importe")
        descripcion = request.POST.get("descripcion")
        departamento = request.POST.get("departamento")
        dep=Departamento.objects.get(pk=departamento)
        #imagen= request.POST.get('imagen')





        #func = Funcionario.objects.get(codigo=Funcionario.codigo)
        
        det = Doctos(
            solicitud=enc,
            tipo_comprobante=tipo_comprobante,
            no_facturasol=no_facturasol,
            fecha_compra=fecha_compra,
            importe=importe,
            departamento=dep,
            descripcion=descripcion,
            #imagen=imagen,
            
        )
        
        if det:
            det.save()
            
        
            return redirect("dto:spyors_edit",contrato_id=contrato_id)

    return render(request,template_name,contexto)