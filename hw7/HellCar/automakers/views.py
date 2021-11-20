from rest_framework import viewsets
from automakers.models import AutoMaker
from automakers.serializers import AutoMakerSerializer


class AutoMakerViewSet(viewsets.ModelViewSet):
    queryset = AutoMaker.objects.all()
    serializer_class = AutoMakerSerializer
