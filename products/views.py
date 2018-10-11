from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status
from django.urls import reverse

from .models import Product
from .serializers import ProductsSerializer

class ListCreateProductsView(generics.ListCreateAPIView):
    """
    GET songs/
    POST songs/
    """
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer

    # @validate_request_data
    def post(self, request, *args, **kwargs):
        a_product = Product.objects.create(
            name=request.data["name"],
            price=request.data["price"],
            description=request.data["description"]
        )
        return Response(
            data=ProductsSerializer(a_product).data,
            status=status.HTTP_201_CREATED
        )

    def get(self, request, *args, **kwargs):
        products = self.queryset.all()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)