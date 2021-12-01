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


class CreateOrderOnCheckoutAPIView(generics.CreateAPIView):
    serializer_class = CreateOrderSerializer

