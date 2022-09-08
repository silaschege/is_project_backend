from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import ManufactureRegisterModel

class ManuFacturerRegisterSerializer(serializers.Serializer):
    class Meta:
        model =  ManufactureRegisterModel
        fields = "__all__"