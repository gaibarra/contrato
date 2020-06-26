from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
#from .reportes import imprimir_solicitud, imprimir_archivos

urlpatterns = [
    path('departamentos/',DepartamentoView.as_view(), name="departamento_list"),
    path('departamentos/new',DepartamentoNew.as_view(), name="departamento_new"),
    path('departamentos/<int:pk>',DepartamentoEdit.as_view(), name="departamento_edit"),
    path('departamentos/estado/<int:id>',departamentoInactivar, name="departamento_inactivar"),
    
    
 
    
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns