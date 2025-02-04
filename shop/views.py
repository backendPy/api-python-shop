from django.shortcuts import render
from rest_framework import viewsets
from .models import Shirt, Pants, Shorts, Cap
from .serializers import ShirtSerializer, PantsSerializer, ShortsSerializer, CapSerializer

class ShirtViewSet(viewsets.ModelViewSet):
    queryset = Shirt.objects.all()
    serializer_class = ShirtSerializer

class PantsViewSet(viewsets.ModelViewSet):
    queryset = Pants.objects.all()
    serializer_class = PantsSerializer

class ShortsViewSet(viewsets.ModelViewSet):
    queryset = Shorts.objects.all()
    serializer_class = ShortsSerializer

class CapViewSet(viewsets.ModelViewSet):
    queryset = Cap.objects.all()  # Corrigido para Cap
    serializer_class = CapSerializer
