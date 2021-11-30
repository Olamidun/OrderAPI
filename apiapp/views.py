from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .serializers import CreateOrderSerializer, ListitemsSerializer
from rest_framework import generics, status
from rest_framework.views import APIView
from .models import Item
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator
# Create your views here.

class ListItemAPIView(generics.ListAPIView):
    serializer_class = ListitemsSerializer

    def get_queryset(self):
        return Item.objects.all()


@method_decorator(name='post', decorator=swagger_auto_schema(
    description='''Endpoint for sellers to view all items they have put up for sale. Requires token authentication in this format: "Bearer <access_token returned by the login endpoint>"'''
))
class CreateOrderOnCheckoutAPIView(generics.CreateAPIView):
    serializer_class = CreateOrderSerializer

