from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer


















































# class ProductDetailAPIView(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# class ProductListAPIView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
# class ProductListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#     def perform_create(self, serializer):
#         serializer.validated_data['name'] = float(serializer.validated_data['name'])
#         serializer.validated_data['description'] = float(serializer.validated_data['description'])
#         serializer.validated_data['price'] = float(serializer.validated_data['price'])
#
#
#         serializer.save()
#
