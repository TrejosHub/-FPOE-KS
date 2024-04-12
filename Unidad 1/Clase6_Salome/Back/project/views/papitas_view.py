from rest_framework.response import Response
from rest_framework.views import APIView
from project.serializers.papitas_serializer import PapitasSerializers
from api.models.papitas import Papitas
from rest_framework import status
from django.http import Http404
    

class Papitas_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        papitas = Papitas.objects.all()
        serializer = PapitasSerializers(papitas, many=True)
        
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = PapitasSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Papitas_APIView_Detail(APIView):
    def get_object(self, pk):
        try:
            return Papitas.objects.get(pk=pk)
        except Papitas.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        papitas = self.get_object(pk)
        serializer = PapitasSerializers(papitas)  
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        papitas = self.get_object(pk)
        serializer = PapitasSerializers(papitas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        papitas = self.get_object(pk)
        papitas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)