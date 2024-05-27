from rest_framework import serializers
from api.models.papitas import Papitas

class PapitasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Papitas
        fields =['id', 'marca', 'sabor', 'color', 'cantidad']
