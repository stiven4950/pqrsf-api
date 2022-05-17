from rest_framework import generics, mixins, status

from .models import City, Matter, Agency
from core.serializers import AgencySerializer, CitySerializer, MatterSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

class CityView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    ):

    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [AllowAny]

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        
        for i in request.data:
            City.objects.create(municipioId=i.get('municipioId'), municipioDepartamento=i.get('municipioDepartamento'))

        return Response(status=status.HTTP_201_CREATED)


class AgencyView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    ):

    queryset = Agency.objects.all()
    serializer_class = AgencySerializer
    permission_classes = [AllowAny]

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        
        for i in request.data:
            Agency.objects.create(name=i.get('name'))

        return Response(status=status.HTTP_201_CREATED)

class MatterView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    ):

    queryset = Matter.objects.all()
    serializer_class = MatterSerializer
    permission_classes = [AllowAny]

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        
        for i in request.data:
            Matter.objects.create(matter_type=i.get('matter_type'), name=i.get('name'))

        return Response(status=status.HTTP_201_CREATED)