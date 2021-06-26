from rest_framework import serializers
from .models import *

class EssaySerializer(serializers.ModelSerializer):
    class Meta:
        model=Essay
        fields=(
            'id',
            'text',
            'score',
        )