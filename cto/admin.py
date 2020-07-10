from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class SecuenciaResource(resources.ModelResource):
    class Meta:
        model = Secuencia

class SecuenciaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['textoSecuencia']
    list_display = ('tipocontrato', 'nivel1', 'nivel2', 'nivel3','nivel4', 'identificador','textoSecuencia')
    resource_class = SecuenciaResource

admin.site.register(Secuencia, SecuenciaAdmin)

class DepartamentoResource(resources.ModelResource):
    class Meta:
        model = Departamento

class DepartamentoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['departamento']
    list_display = ('clavedepto', 'departamento')
    resource_class = DepartamentoResource

admin.site.register(Departamento, DepartamentoAdmin)

class PartesResource(resources.ModelResource):
    class Meta:
        model = Partes

class PartesAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombreParte']
    list_display = ('nombreParte','nombresParte', 'apellidoPaternoParte', 'apellidoMaternoParte' )
    resource_class = PartesResource

admin.site.register(Partes, PartesAdmin)


admin.site.register(Ciclos)
admin.site.register(Tipocontrato)
admin.site.register(Contratos)
admin.site.register(Estados)
admin.site.register(Niveles)
admin.site.register(Profesiones)