from dandhacontrol.models import Locality
from dandhacontrol.serializers import LocalitySerializer
from rest_framework import generics




class LocalityListCreateView(generics.ListCreateAPIView):
    queryset = Locality.objects.all()
    serializer_class = LocalitySerializer
    # permission_classes = (IsAuthenticatedOrReadOnly, )


class LocalityRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Locality.objects.all()
    serializer_class = LocalitySerializer
    # permission_classes = (IsAuthenticatedOrReadOnly, )

