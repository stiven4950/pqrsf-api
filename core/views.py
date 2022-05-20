from rest_framework import generics, mixins, status

from .models import City, FileUser, Matter, Agency, UserPqrsf
from core.serializers import AgencySerializer, CitySerializer, MatterSerializer, UserPqrsfSerializer
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

class UserView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    ):

    queryset = UserPqrsf.objects.all()
    serializer_class = UserPqrsfSerializer
    permission_classes = [AllowAny]


    def get(self, request):
        return self.list(request)
    
    def post(self, request):

        data = request.data
        user_type = data.get('user_type')
        request_type = data.get('request_type')
        id_matter = data.get('matter')
        matter = Matter.objects.get(id=id_matter)
        files = data.get('files')

        user = object()

        if user_type == 1:
            
            document_type = data.get('document_type')
            document_number = data.get('document_number')
            fullname = data.get('fullname')
            telephone = data.get('telephone')
            phone = data.get('phone')
            email = data.get('email')
            id_city = data.get('city')
            address = data.get('address')
            associate = data.get('associate')
            id_agency = data.get('agency')
            request_type = data.get('request_type')
            id_matter = data.get('matter')
            medium = data.get('medium')
            description = data.get('description')

            # Search for City, Agency and Matter
            city = City.objects.get(id=id_city)
            agency = Agency.objects.get(id=id_agency)
            matter = Matter.objects.get(id=id_matter)



            user = UserPqrsf.objects.create(
                document_type=document_type,
                document_number=document_number,
                fullname=fullname,
                telephone=telephone,
                phone=phone,
                email=email,
                city=city,
                address=address,
                associate=associate,
                agency=agency,
                request_type=request_type,
                matter=matter,
                medium=medium,
                description=description,
            )

        else:
            fullname = data.get('fullname')
            description = data.get('description')
            files = data.get('files')

            UserPqrsf.objects.create(
                fullname=fullname,
                request_type=request_type,
                matter=matter,
                description=description,
            )

        if len(files)>0:
            for i in files:
                file = FileUser.objects.create(name=i.name, filetype=i.filetype, path=i.path)
                user.files.add(file)
            
        user.save()

        return Response(status=status.HTTP_201_CREATED)
