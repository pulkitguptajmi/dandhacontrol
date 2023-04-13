from dandhacontrol.models import Package, CompanyServiceRelationship
from dandhacontrol.serializers import PackageSerializer
from rest_framework import generics




class PackageListCreateView(generics.ListCreateAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly, )


class PackageRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly, )
