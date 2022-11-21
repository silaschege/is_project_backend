from rest_framework import serializers
from .models import LandRegisterModel

class LandRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandRegisterModel
        field = "__all__"