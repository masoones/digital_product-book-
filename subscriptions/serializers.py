from rest_framework import serializers

from .models import Package,Subscription

class PackageSerializer(serializers.ModelSerializer):
    model = Package
    fields = ['title','sku','avatar','description','price','duration']

class SubscriptionSerializer(serializers.ModelSerializer):
    package = PackageSerializer()

    class Meta:
        model = Subscription
        fields = ['pakage','created_time','expire_time']


