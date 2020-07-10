from django import forms

from .models import Departamento, Partes




class DepartamentoForm(forms.ModelForm):
    class Meta:
        model=Departamento
        fields=['clavedepto','departamento','f001', 'f002','f003','estado']
        exclude = ['um','fm','uc','fc']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class PartesForm(forms.ModelForm):
    
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
    
    
    clavedepto = forms.ModelChoiceField(
        queryset=Departamento.objects.filter(estado=True)
        .order_by('departamento')
    )
    
    
    class Meta:
        model =Partes
        fields=['codigo','clavedepto', 'tituloParte', 'nombresParte', 'apellidoPaternoParte', 'apellidoMaternoParte','fecha_ingreso', 'email', 'lugarnacimientoParte', 'rfc', 'imss', 'curp','regfiscalParte', 'cedula_profParte', 'titulo_profParte', 'universidadParte','domicilioParte', 'phone', 'mobile','grupo_sanguineo','alergias']
        exclude = ['um','fm','uc','fc']
    
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

        self.fields['codigo'].widget.attrs['style'] = "width:100px"
        self.fields['codigo'].widget.attrs['readonly'] = True
        self.fields['clavedepto'].widget.attrs['style'] = "width:540px"
        self.fields['tituloParte'].widget.attrs['style'] = "width:110px"
        self.fields['apellidoPaternoParte'].widget.attrs['style'] = "width:160px"
        self.fields['apellidoMaternoParte'].widget.attrs['style'] = "width:160px"
        self.fields['titulo_profParte'].widget.attrs['style'] = "width:300px"
        self.fields['universidadParte'].widget.attrs['style'] = "width:400px"  
        self.fields['cedula_profParte'].widget.attrs['style'] = "width:200px"  
        self.fields['domicilioParte'].widget.attrs['verbose_name'] = "Domicilio"   
    
