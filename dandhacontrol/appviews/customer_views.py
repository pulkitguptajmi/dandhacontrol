from dandhacontrol.models import Customer
from dandhacontrol.serializers import CustomerSerializer
from rest_framework import generics




class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly, )


class CustomerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly, )