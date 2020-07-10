from ckeditor.fields import RichTextField
from djmoney.models.fields import MoneyField
from djmoney.money import Money
from django.utils import timezone


from django.db import models
from django.contrib.auth.models import User

#Para los signals
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum

from bases.models import ClaseModelo, ClaseModelo2




class Departamento(ClaseModelo):
    clavedepto = models.IntegerField(unique=True)
    departamento = models.CharField(max_length=200)
    f001 = models.CharField('Formato1', max_length=60, blank=True, null=True)
    f002 = models.CharField('Formato2', max_length=60, blank=True, null=True)
    f003 = models.CharField('Formato3', max_length=60, blank=True, null=True)
    f004 = models.CharField('Formato4', max_length=60, blank=True, null=True)
    f005 = models.CharField('Formato5', max_length=60, blank=True, null=True)
    f006 = models.CharField('Formato6', max_length=60, blank=True, null=True)
    f007 = models.CharField('Formato7', max_length=60, blank=True, null=True)
    f008 = models.CharField('Formato8', max_length=60, blank=True, null=True)
    f009 = models.CharField('Formato9', max_length=60, blank=True, null=True)
    f010 = models.CharField('Formato10', max_length=60, blank=True, null=True)
    f011 = models.CharField('Formato11', max_length=60, blank=True, null=True)
    f012 = models.CharField('Formato12', max_length=60, blank=True, null=True)
    f013 = models.CharField('Formato13', max_length=60, blank=True, null=True)
    f014 = models.CharField('Formato14', max_length=60, blank=True, null=True)
    f015 = models.CharField('Formato15', max_length=60, blank=True, null=True)
    f016 = models.CharField('Formato16', max_length=60, blank=True, null=True)
    f017 = models.CharField('Formato17', max_length=60, blank=True, null=True)
    f018 = models.CharField('Formato18', max_length=60, blank=True, null=True)
    f019 = models.CharField('Formato19', max_length=60, blank=True, null=True)
    f020 = models.CharField('Formato20', max_length=60, blank=True, null=True)
    f021 = models.CharField('Formato21', max_length=60, blank=True, null=True)
    f022 = models.CharField('Formato22', max_length=60, blank=True, null=True)
    f023 = models.CharField('Formato23', max_length=60, blank=True, null=True)
    f024 = models.CharField('Formato24', max_length=60, blank=True, null=True)
    f025 = models.CharField('Formato25', max_length=60, blank=True, null=True)
    f026 = models.CharField('Formato26', max_length=60, blank=True, null=True)
    f027 = models.CharField('Formato27', max_length=60, blank=True, null=True)
    f028 = models.CharField('Formato28', max_length=60, blank=True, null=True)
    f029 = models.CharField('Formato29', max_length=60, blank=True, null=True)
    f030 = models.CharField('Formato30', max_length=60, blank=True, null=True)
    f031 = models.CharField('Formato31', max_length=60, blank=True, null=True)
    f032 = models.CharField('Formato32', max_length=60, blank=True, null=True)
    f033 = models.CharField('Formato33', max_length=60, blank=True, null=True)
    f034 = models.CharField('Formato34', max_length=60, blank=True, null=True)
    f035 = models.CharField('Formato35', max_length=60, blank=True, null=True)
    f036 = models.CharField('Formato36', max_length=60, blank=True, null=True)
    f037 = models.CharField('Formato37', max_length=60, blank=True, null=True)
    f038 = models.CharField('Formato38', max_length=60, blank=True, null=True)
    f039 = models.CharField('Formato39', max_length=60, blank=True, null=True)
    f040 = models.CharField('Formato40', max_length=60, blank=True, null=True)
    f041 = models.CharField('Formato41', max_length=60, blank=True, null=True)
    f042 = models.CharField('Formato42', max_length=60, blank=True, null=True)
    f043 = models.CharField('Formato43', max_length=60, blank=True, null=True)
    f044 = models.CharField('Formato44', max_length=60, blank=True, null=True)
    f045 = models.CharField('Formato45', max_length=60, blank=True, null=True)
    f046 = models.CharField('Formato46', max_length=60, blank=True, null=True)
    f047 = models.CharField('Formato47', max_length=60, blank=True, null=True)
    f048 = models.CharField('Formato48', max_length=60, blank=True, null=True)
    f049 = models.CharField('Formato49', max_length=60, blank=True, null=True)
    f050 = models.CharField('Formato50', max_length=60, blank=True, null=True)
    departamento2 = models.CharField(max_length=200, default="")



    def __str__(self):
        
        return self.departamento

    def save(self):
        self.departamento = self.departamento.upper()
        super(Departamento, self).save()

    class Meta:
        verbose_name_plural = "Departamentos"

  
class Partes(ClaseModelo2):
    codigo = models.CharField('Código', max_length=13, blank=True, null=True)
    clave_depto = models.IntegerField('Clave de Depto.', null=True)
    fecha_ingreso = models.DateField('Fecha de ingreso', blank=True, null=True)
    email = models.EmailField('Correo electrónico', blank=True, null=True)
    tituloParte = models.CharField('Título ', max_length=100, blank=True, null=True)
    nombreParte = models.CharField('Nombre o razón social ', max_length=200, blank=False, null=False)
    nombresParte = models.CharField('Nombres del contratante', max_length=100, blank=True, null=True)
    apellidoPaternoParte = models.CharField('Apellido paterno', max_length=100, blank=True, null=True)
    apellidoMaternoParte = models.CharField('Apellido materno', max_length=100, blank=True, null=True)
    lugarnacimientoParte = models.CharField('Lugar de nacimiento ', max_length=100, blank=True, null=True)
    acta_nac_constimgParte = models.FileField('Acta de nacimiento', upload_to='media/', default = 'None/no-img.jpg')
    rfc = models.CharField('RFC', max_length=13, blank=True, null=True)
    rfc_imgParte = models.FileField('Cédula del R.F.C', upload_to='media/', default = 'None/no-img.jpg')
    imss = models.CharField('IMSS', max_length=11, blank=True, null=True)
    rimss_imgParte = models.FileField('Constancia IMSS', upload_to='media/', default = 'None/no-img.jpg')
    curp = models.CharField('CURP', max_length=18, blank=True, null=True)
    curp_imgParte = models.FileField('CURP', upload_to='media/', default = 'None/no-img.jpg')
    regfiscalParte = models.CharField('Régimen fiscal ', max_length=200, blank=True, null=True)
    cedula_fiscalimgParte = models.FileField('Constancia Régimen fiscal', upload_to='media/', default = 'None/no-img.jpg')
    idrep_legalParte = models.IntegerField('id Representante legal', blank=True, null=True)
    datos_actaconstParte = RichTextField('Datos acta constitutiva', blank=True, null=True)
    titulo_profParte = models.CharField('Título profesional', max_length=100, blank=True, null=True)
    titulo_profimgParte  = models.FileField('Título profesional', upload_to='media/', default = 'None/no-img.jpg')
    universidadParte =  models.CharField('Universidad', max_length=100, blank=True, null=True)
    cedula_profParte = models.CharField('Cédula profesional', max_length=100, blank=True, null=True)
    cedula_profimgParte  = models.FileField('Cédula profesional', upload_to='media/', default = 'None/no-img.jpg')
    domicilioParte = RichTextField('Domicilio', blank=True, null=True)
    comp_domimgParte  = models.FileField('Comprobante de domicilio', upload_to='media/', default = 'None/no-img.jpg')
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank = True, null = True)
    usuario = models.CharField('Usuario', max_length=50, blank=True, null=True)
    phone = models.CharField('Teléfono', max_length=13, blank=True, null=True)
    mobile = models.CharField('Movil', max_length=13, blank=True, null=True)
    grupo_sanguineo = models.CharField('Grupo sanguíneo', max_length=50, blank=True, null=True)
    alergias = models.CharField('Alergias', max_length=100, blank=True, null=True)
    
    def __str__(self):
        return '{}'.format(self.id)

    def save(self):
        super(Partes,self).save()

    class Meta:
        verbose_name_plural = "Parte del contrato"
        verbose_name="Partes del contrato"

class Ciclos(ClaseModelo2):
    descripcionCiclo = models.CharField('Descripción del ciclo', max_length=150, blank=False, null=False)
    date_ini = models.DateTimeField('Fecha inicial del ciclo', blank=True, null=True)
    date_fin = models.DateTimeField('Fecha final del ciclo', blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.descripcionCiclo)

    def save(self):
        super(Ciclos,self).save()

    class Meta:
        verbose_name_plural = "Ciclos escolares"
        verbose_name="Ciclo escolar"

class Tipocontrato(ClaseModelo2):
    tipoContrato = models.CharField('Tipo de contrato', max_length=150, blank=False, null=False)
    tituloContrato = RichTextField('Título del Contrato', blank=False, null=False)
    textoinicialContrato = RichTextField('Texto inicial del Contrato', blank=False, null=False)
    descripcionContrato = RichTextField('Descripción del Contrato', blank=True, null=True)
    marcatipoContrato = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.tipoContrato)

    def save(self):
        super(Tipocontrato,self).save()

    class Meta:
        verbose_name_plural = "Tipos de contrato"
        verbose_name="Tipo de contrato"

class Contratos(ClaseModelo2):
    tipocontrato = models.ForeignKey(Tipocontrato, on_delete=models.CASCADE)
    datecontrato = models.DateTimeField('Fecha del contrato', blank=True, null=True)
    datecontrato_ini = models.DateTimeField('Fecha inicial de la vigencia', blank=True, null=True)
    datecontrato_fin = models.DateTimeField('Fecha final de la vigencia', blank=True, null=True)
    parte1 = models.IntegerField('Parte 1', blank=True, null=True, default=3 )
    enCalidadDe1 = models.CharField('En calidad de 1', max_length=150, blank=False, null=False)
    parte2 = models.ForeignKey(Partes, on_delete=models.CASCADE)
    enCalidadDe2 = models.CharField('En calidad de 2', max_length=150, blank=False, null=False)
    #parte3 = models.ForeignKey(Partes, on_delete=models.CASCADE)
    #enCalidadDe3 = models.CharField('En calidad de 3', max_length=150, blank=True, null=True)
    lugarContrato = RichTextField('Lugar del Contrato', blank=True, null=True)
    ciudadContrato = models.CharField('Usuario', max_length=50, blank=True, null=True)
    estadoContrato = models.CharField('Usuario', max_length=50, blank=True, null=True)
    paisContrato = models.CharField('Usuario', max_length=50, blank=True, null=True)
    importeContrato = MoneyField('Importe del Contrato', max_digits=14, decimal_places=2, blank=False, null=False, default_currency="MXN")
    npContrato = models.IntegerField('Número de pagos', blank=True, null=True)
    imppContrato = MoneyField('Importe de cada pago', max_digits=14, decimal_places=2, blank=False, null=False, default_currency="MXN")
    totalhorasContrato = models.IntegerField('Número de pagos', blank=True, null=True)
    testigoContrato1 = models.CharField('Testigo 1', max_length=100, blank=True, null=True)
    testigoContrato2 = models.CharField('Testigo 2', max_length=100, blank=True, null=True)
    versionContrato = models.CharField('Versión del contrato', max_length=100, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.id)

    def save(self):
        super(Contratos,self).save()

    class Meta:
        verbose_name_plural = "Contratos"
        verbose_name="Contrato"


class Secuencia(ClaseModelo2):
    tipocontrato = models.ForeignKey(Tipocontrato, on_delete=models.CASCADE)
    nivel1 = models.IntegerField('Nivel 1', blank=True, null=True)
    nivel2 = models.IntegerField('Nivel 2', blank=True, null=True)
    nivel3 = models.IntegerField('Nivel 3', blank=True, null=True)
    nivel4 = models.IntegerField('Nivel 4', blank=True, null=True)
    identificador = models.CharField('Identificador', max_length=10, blank=True, null=True)
    textoSecuencia = RichTextField('Texto secuencia', blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.tipocontrato)

    def save(self):
        super(Secuencia,self).save()

    class Meta:
        verbose_name_plural = "Secuencia del contrato"
        verbose_name="Secuencia del contrato"
        
class Estados(ClaseModelo2):
    claveEstado = models.CharField('Clave del Estado', max_length=2, blank=False, null=False)
    nombreEstado = models.CharField('Numbre del Estado', max_length=50, blank=False, null=False)
   

    def __str__(self):
        return '{}'.format(self.nombreEstado)

    def save(self):
        super(Estados,self).save()

    class Meta:
        verbose_name_plural = "Estados"
        verbose_name="Estado"

class Niveles(ClaseModelo2):
    nivel = models.CharField('Nivel Escolar', max_length=50, blank=False, null=False)
    
    def __str__(self):
        return '{}'.format(self.nivel)

    def save(self):
        super(Niveles,self).save()

    class Meta:
        verbose_name_plural = "Niveles"
        verbose_name="Nivel"

class Profesiones(ClaseModelo2):
    abrevProfesion = models.CharField('Abreviatura', max_length=20, blank=False, null=False)
    descProfesion = models.CharField('Profesión', max_length=100, blank=False, null=False)
    
    def __str__(self):
        return '{}'.format(self.descProfesion)

    def save(self):
        super(Profesiones,self).save()

    class Meta:
        verbose_name_plural = "Profesiones"
        verbose_name="Profesión"


class Puestos(ClaseModelo2):
    nombrePuesto = models.CharField('Nombre Puesto', max_length=100, blank=False, null=False)
    claveCampus = models.CharField('Clave del Campus', max_length=3, blank=False, null=False)
    impHora = MoneyField('Importe por Hora', max_digits=14, decimal_places=2, blank=False, null=False, default_currency="MXN")

    def __str__(self):
        return '{}'.format(self.nombrePuesto)

    def save(self):
        super(Puestos,self).save()

    class Meta:
        verbose_name_plural = "Puestos"
        verbose_name="Puesto"                                                                     