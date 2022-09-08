from django.contrib.auth import get_user_model
User = get_user_model()
from .models import LandRegisterModel
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions,status
from .serializer import LandRegisterSerializer
from rest_framework import serializers

# Create your views here.
# register a land 
# update land size not location 
# delete a land 

class LandRegisterCreateView(APIView):
    def post(self,request):
        try:
            data=request.data

            country = data['country']
            sub_county = data['sub_county']
            village = data['village']
            landSize = data['landSize']
            
            if((request.user.is_farmer)==True):
                LandRegisterModel.objects.create(
                    country = country,
                    sub_county = sub_county,
                    village = village,
                    landSize = landSize,
                    user = request.user
                )
            

        except:
            return Response(
                    {'ERROR':'Unable to add land'},
                    status =  status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class LandRegisterUpdateView():
    queryset = LandRegisterModel.objects.all()
    serializer_class = LandRegisterSerializer
    permission_classes = (permissions.IsAuthenticated,)

    # def update(self, request, *args, **kwargs):
    #     data = self.get_object()
    #     data.name = request.data.get("name")
    #     data.save()

    #     serializer = self.get_serializer(data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)

    #     return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        land_objects = LandRegisterModel.objects.get()
        permission_classes = (permissions.IsAuthenticated,)
        data = request.data

        land_objects.landSize = data['landSize']

        land_objects.save()
        return Response(serializer.data)

class LandRegisterDeleteView():
    def delete(self, request):
        try:
            data = request.data

            id = data['id']

            if not LandRegisterModel.objects.filter(id=id).exists():
                return Response(
                        {'Error':'Land you are trying to delete does not exist'},
                        status=status.HTTP_404_NOT_FOUND
                    
                )
            
            LandRegisterModel.objects.filter(id=id).delete()

            if not LandRegisterModel.objects.filter(id=id).exists():
                return Response(
                    {'Success':'Land deleted succesfully'},
                    status=status.HTTP_204_NO_CONTENT
                )
            else:
                return Response(
                    {'Error':'Failed to delete land'},
                    status=status.HTTP_400_BAD_REQUEST
                )

        except:
            return Response(
                {'error': 'Something went wrong when deleting land'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
