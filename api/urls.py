from django.urls import path, include
from .views import *

urlpatterns = [
    path('v1/partes/',PartesList.as_view(),name='partes_list'),
    path('v1/partes/<str:codigo>',PartesDetalle.as_view(),name='partes_detalle'),
]