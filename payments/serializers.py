from rest_framework import serializers

from .models import Gateway

class GatewaySerializer(serializers.ModelSerializer):
    model = Gateway
    fields = ['id','title','descriptions','avatar']

