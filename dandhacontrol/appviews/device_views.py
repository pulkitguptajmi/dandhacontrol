from dandhacontrol.models import Device
from dandhacontrol.serializers import DeviceSerializer
from rest_framework import generics




class DeviceListCreateView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly, )


class DeviceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly, )
