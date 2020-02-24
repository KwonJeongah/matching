from .models import Point, ResultLink
from rest_framework import serializers, viewsets

class PointSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Point
        fields = '__all__'

class PointViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.all()
    serializer_class = PointSerializer

class ResultLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultLink
        fields = '__all__'

class ResultLinkViewSet(viewsets.ModelViewSet):
    queryset = ResultLink.objects.all()
    serializer_class = ResultLinkSerializer