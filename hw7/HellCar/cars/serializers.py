from rest_framework import serializers

from automakers.models import AutoMaker
from cars.models import Car
from users.models import User


class CarSerializer(serializers.ModelSerializer):
    creator = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        required=True,
        slug_field='username',
    )
    make = serializers.SlugRelatedField(
        queryset=AutoMaker.objects.all(),
        required=True,
        slug_field='name',
    )

    def validate_price(self, value):
        if float(value) < 0:
            raise serializers.ValidationError("Price can not be negative!")
        return value

    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'type_of_drive', 'price', 'year', 'comment', 'creator']
