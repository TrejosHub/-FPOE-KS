from rest_framework.response import Response
from rest_framework.views import APIView
from api.models.servicio import Servicio
from project.serializers.servicio_serializer import ServicioSerializers
from rest_framework import status
from django.http import Http404

class Servicio_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        servicio = Servicio.objects.all()
        serializer = ServicioSerializers(servicio, many=True)
        
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = ServicioSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Servicio_APIView_Detail(APIView):
    def get_object(self, pk):
        try:
            return Servicio.objects.get(pk=pk)
        except Servicio.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        servicio = self.get_object(pk)
        serializer = ServicioSerializers(servicio)  
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        servicio = self.get_object(pk)
        serializer = ServicioSerializers(servicio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        servicio = self.get_object(pk)
        servicio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)