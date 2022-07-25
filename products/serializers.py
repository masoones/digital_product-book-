from rest_framework import serializers

from .models import Category , Product , ProductFile

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','title','description','avatar')

class ProductFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFile
        fields = ('id','title','file')

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializer(many=True)
    #files = ProductFileSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id','title','description','avatar','categories','url')#,'files'



