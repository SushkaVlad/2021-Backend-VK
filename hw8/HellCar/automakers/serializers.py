import re

from rest_framework import serializers
from automakers.models import AutoMaker


class AutoMakerSerializer(serializers.ModelSerializer):

    def validate_name(self, value):
        if not re.search(r"^[a-zA-z.-]+$", value):
            raise serializers.ValidationError("Incorrect name!")
        return value

    class Meta:
        model = AutoMaker
        fields = ['id', 'name', 'foundation_year', 'location', 'comment']
