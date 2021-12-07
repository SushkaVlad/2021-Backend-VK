from django.utils.decorators import method_decorator
from rest_framework import viewsets

from application.views import login_is_required
from cars.models import Car
from cars.serializers import CarSerializer


@method_decorator(login_is_required, name='dispatch')
class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        user = self.request.user
        return Car.objects.filter(creator=user)
