from xml.parsers.expat import model
from rest_framework import viewsets
from .models import PaymentLogModel
from .serializers import PaymentLogSerializer

class PaymentLogViewSet(viewsets.ModelViewSet):
    queryset = PaymentLogModel.objects.all()
    serializer = PaymentLogSerializer