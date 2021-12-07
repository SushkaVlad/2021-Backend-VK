from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.response import Response

from application.views import login_is_required
from automakers.models import AutoMaker
from automakers.serializers import AutoMakerSerializer


@method_decorator(login_is_required, name='dispatch')
class AutoMakerViewSet(viewsets.ModelViewSet):

    serializer_class = AutoMakerSerializer
    queryset = AutoMaker.objects.all()

    # def list(self, request):
    #     print(request.user)
    #     return Response(self.serializer_class(self.queryset, many=True).data)
