from .models import Tipocontrato
from django.db import transaction


class CtoMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response
     

    def __call__(self, request):
        #print(request.META)
        self.process_request(request)
        response = self.get_response(request)
        return response

    # def process_view(self,request, view_func, view_args, view_kwargs):
    #     url = request.META.get('PATH_INFO')
    #     #print(url) 
    #     if request.user.is_authenticated:
    #         if 'api' in url:
    #              xid = (view_kwargs['id'])
    #              #print (xid)
    #              #print('esta es', request, view_func, view_args, view_kwars)
    #              tipocontrato = Tipocontrato.objects.filter(estado=True)
    #              for tipo in tipocontrato:
    #                  #print(type(tipo.id))
    #                  #print(type(xid))
    #                  if str(tipo.id) == xid:
    #                     tipo.marcatipoContrato = True
    #                     tipo.save()
    #                  else:
    #                     tipo.marcatipoContrato = False
    #                     tipo.save()

    def process_request(self, request):
       
        #print(xpet)
        #print(type(xpet))
        #print ('aqui estoy', request.body)

        url = request.META.get('PATH_INFO')
        print(url) 
        #if request.user.is_authenticated:
        if "api" in url:
            xpet = request.body.decode("utf-8")
            xid = xpet

            with transaction.atomic():
                # Establecer todos los objetos Tipocontrato a False
                Tipocontrato.objects.update(marcatipoContrato=False)

                # Buscar el objeto con el id que coincide con xid y establecer su marcatipoContrato a True
                tipocontrato = Tipocontrato.objects.filter(estado=True, id=xid).first()
            if tipocontrato:
                tipocontrato.marcatipoContrato = True
                tipocontrato.save()

        return None
