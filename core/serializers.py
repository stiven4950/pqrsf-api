from rest_framework import serializers

from .models import City, Agency, FileUser, Matter, UserPqrsf


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class AgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Agency
        fields = '__all__'


class MatterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matter
        fields = '__all__'


class FileUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUser
        fields = '__all__'


class UserPqrsfSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPqrsf
        depth = 2
        fields = '__all__'
