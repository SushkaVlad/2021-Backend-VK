from django.utils.decorators import method_decorator
from rest_framework import viewsets

from application.views import login_is_required
from users.models import User
from users.serializers import UserSerializer


@method_decorator(login_is_required, name='dispatch')
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
