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

    def to_internal_value(self, data):
        if data.get('text',None) == "":  
            return serializers.ValidationError("Atleast One Answer must be provided")
        return super(EssaySerializer, self).to_internal_value(data)