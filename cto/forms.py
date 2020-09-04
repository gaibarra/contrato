from django import forms
from django.contrib.auth.models import User 
from .models import Departamento, Partes, Contratos




class DepartamentoForm(forms.ModelForm):
    class Meta:
        model=Departamento
        fields=['claveDepartamento','claveCampus','claveArea','nombreDepartamento','f001', 'f002','f003','estado']
        exclude = ['um','fm','uc','fc']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class PartesForm(forms.ModelForm):
        
    
    claveDepartamento = forms.ModelChoiceField(
        queryset=Departamento.objects.filter(estado=True)
            .order_by('claveDepartamento')
        )
    
    domicilioParte = forms.CharField(
            widget=forms.Textarea(
                attrs={
                    "rows": 3,
                    "cols": 80,
                    "placeholder": "Domicilio completo",
                    "verbose_name": "Domicilio",
                    }
                )
            )
    class Meta:
        model =Partes
        fields=['claveDepartamento','codigo', 'tituloParte', 'nombresParte', 'apellidoPaternoParte', 'apellidoMaternoParte','fecha_ingreso', 'email', 'lugarnacimientoParte', 'rfc', 'imss', 'curp','regfiscalParte', 'cedula_profParte', 'titulo_profParte', 'universidadParte','domicilioParte', 'phone', 'mobile','grupo_sanguineo','alergias']
        exclude = ['um','fm','uc','fc']
    
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

        self.fields['codigo'].widget.attrs['style'] = "width:100px"
        self.fields['codigo'].widget.attrs['readonly'] = True
        self.fields['claveDepartamento'].widget.attrs['style'] = "width:540px"
        self.fields['tituloParte'].widget.attrs['style'] = "width:110px"
        self.fields['apellidoPaternoParte'].widget.attrs['style'] = "width:160px"
        self.fields['apellidoMaternoParte'].widget.attrs['style'] = "width:160px"
        self.fields['titulo_profParte'].widget.attrs['style'] = "width:300px"
        self.fields['universidadParte'].widget.attrs['style'] = "width:400px"  
        self.fields['cedula_profParte'].widget.attrs['style'] = "width:200px"  
        self.fields['domicilioParte'].widget.attrs['verbose_name'] = "Domicilio"

class ContratosForm(forms.ModelForm):
    #fecha_solicitud = forms.DateInput()
    #fecha_cheque = forms.DateInput()
    
    class Meta:
        model=Contratos
        fields=['id','tipocontrato','parte1']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        
        #self.fields['status'].widget.attrs['readonly'] = True
        
        #self.fields['fecha_cheque'].widget.attrs['value'] = datetime.today()
        #self.fields['fecha_solicitud'].widget.attrs['readonly'] = True
        #self.fields['imp_total'].widget.attrs['readonly'] = True
        #self.fields['imp_total'].widget.attrs['style'] = "width:200px"    
