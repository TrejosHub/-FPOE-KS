from rest_framework import serializers
from api.models.silla import Silla

class SillaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Silla
        fields = '__all__'