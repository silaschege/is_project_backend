from xml.parsers.expat import model
from rest_framework import viewsets
from .models import InstallmentModel
from .serializer import InstallmentSerializer

class InstallmentViewSet(viewsets.ModelViewSet):
    queryset = InstallmentModel.objects.all()
    serializer = InstallmentSerializer