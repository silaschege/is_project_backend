from xml.parsers.expat import model
from rest_framework import viewsets
from .models import LandRegisterModel
from .serializer import LandRegisterSerializer

class LandRegisterViewSet(viewsets.ModelViewSet):
    queryset = LandRegisterModel.objects.all()
    serializer = LandRegisterSerializer