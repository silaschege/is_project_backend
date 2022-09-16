from django.shortcuts import render
from .models import ManufactureRegisterModel
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions,status
from .serializer import ManuFacturerRegisterSerializer

# Create your views here.
# register a manufacturer when they are new to the sytem
# update  the manufacturer data in the system
# deleting the manufacturer will happen when you elete the admin maufacturer 

class ManufactureRegisterCreateView (APIView):
    def post(self,request):
        data = request.data

        manufactureName = data['manufactureName']
        email = data['email']
        country = data['country']
        county = data['county']
        location = data['location']

        if(request.user.is_manufacturer)==True:
            ManufactureRegisterModel.objects.create(
                manufactureName = manufactureName,
                email = email,
                country = country,
                location= location,
                user = request.user
            )

class ManufactureRegisterUpdateView (APIView):
    queryset = ManufactureRegisterModel.objects.all()
    serializer_class = ManuFacturerRegisterSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        data = self.get_object()
        data.name = request.data.get("name")
        data.save()



