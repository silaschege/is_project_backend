from dataclasses import fields
from rest_framework import serializers
from .models import InstallmentModel

class InstallmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstallmentModel
        fields = "__all__"