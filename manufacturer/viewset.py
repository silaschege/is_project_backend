from xml.parsers.expat import model
from rest_framework import viewsets
from .models import ManufactureRegisterModel
from .serializer import ManuFacturerRegisterSerializer

class ManufactureRegisterViewSet(viewsets.ModelViewSet):
    queryset = ManufactureRegisterModel.objects.all()
    serializer = ManuFacturerRegisterSerializer