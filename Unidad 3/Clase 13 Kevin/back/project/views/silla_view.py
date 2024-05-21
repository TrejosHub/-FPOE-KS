from rest_framework.response import Response
from rest_framework.views import APIView
from api.models.silla import Silla
#from ..serializers.post_serializer import SillaSerializers
from project.serializers.silla_serializer import SillaSerializers
from rest_framework import status
from django.http import Http404

class Silla_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        queryset = Silla.objects.all()
        material = self.request.query_params.get('material')
        if material is not None:
            queryset = queryset.filter(material = material)
        serializer = SillaSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SillaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Silla_APIView_Detail(APIView):
    def get_object(self, pk):
        try:
            return Silla.objects.get(pk=pk)
        except Silla.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        silla = self.get_object(pk)
        serializer = SillaSerializers(silla)  
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        silla = self.get_object(pk)
        serializer = SillaSerializers(silla, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        silla = self.get_object(pk)
        silla.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)