from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from subscriptions.models import Subscription
from .models import Category , Product ,ProductFile
from .serializers import CategorySerializer , ProductSerializer , ProductFileSerializer


class CategoryListView(APIView):

    def get (self,request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories,many=True, context={'request' : request})
        return Response(serializer.data)

class CategoryDetailListView(APIView):

    def get (self,request,pk):
        try:
            categories = Category.objects.get(pk=pk)
        except Category.DoNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(categories, context={'request' : request})
        return Response(serializer.data)


class ProductListView(APIView):

    def get (self,request):
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True, context={'request' : request})
        return Response(serializer.data)

class ProductDetailListView(APIView):
    permission_classes = [IsAuthenticated]

    def get (self,request,pk):
        if not Subscription.objects.filter(
            user=request.user,
            expire_time__gt=timezone.now()
        ).exists():
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        try:
            products = Product.objects.get(pk=pk)
        except Product.DoNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(products, context={'request' : request})
        return Response(serializer.data)


class ProductFileListView(APIView):

    def get (self,request,product_id):
        productfiles = ProductFile.objects.filter(product_id=product_id)
        serializer = ProductFileSerializer(productfiles,many=True, context={'request' : request})
        return Response(serializer.data)

class ProductFileDetailListView(APIView):

    def get (self,request,pk,product_id):
        try:
            productfiles = ProductsFile.objects.get(pk=pk,product_id=product_id)
        except ProductFile.DoNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProductFileSerializer(productfiles, context={'request' : request})
        return Response(serializer.data)

