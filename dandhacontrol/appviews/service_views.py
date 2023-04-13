from dandhacontrol.models import Service
from dandhacontrol.serializers import ServiceSerializer
from rest_framework.response import Response
from rest_framework import generics


class ServiceListCreateView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly, )


class ServiceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly, )

