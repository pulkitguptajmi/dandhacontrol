from dandhacontrol.models import PaymentMode
from dandhacontrol.serializers import PaymentModeSerializer
from rest_framework import generics




class PaymentModeListCreateView(generics.ListCreateAPIView):
    queryset = PaymentMode.objects.all()
    serializer_class = PaymentModeSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly, )


class PaymentModeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentMode.objects.all()
    serializer_class = PaymentModeSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly, )
