from rest_framework import serializers

from .models import City, Agency, Matter

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