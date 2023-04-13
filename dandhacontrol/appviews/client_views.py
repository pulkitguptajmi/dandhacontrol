from dandhacontrol.models import Client
from dandhacontrol.serializers import ClientSerializer
from rest_framework.response import Response
from rest_framework import generics


class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
