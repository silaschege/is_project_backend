from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import PaymentLogModel

class PaymentLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentLogModel
        fields = "__all__"