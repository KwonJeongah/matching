from .models import Coords, ResultLink
from rest_framework import serializers, viewsets

class CoordsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Coords
        fields = '__all__'

class CoordsViewSet(viewsets.ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer

class ResultLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultLink
        fields = '__all__'

class ResultLinkViewSet(viewsets.ModelViewSet):
    queryset = ResultLink.objects.all()
    serializer_class = ResultLinkSerializer