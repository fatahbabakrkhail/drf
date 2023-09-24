from django.forms import model_to_dict
from django.http import JsonResponse
from product.models import Product
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.serializers import ProductSerializer


@api_view(['POST'])
def api_view(request, *args, **kwargs):

    # product = Product.objects.all().first()
    # data = {}
    # if product:
    serializers= ProductSerializer(data=request.data)
    if serializers.is_valid():
        data=serializers.save()
        return Response(serializers.data)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)