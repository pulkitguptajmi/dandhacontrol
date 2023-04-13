from dandhacontrol.models import Recharge
from dandhacontrol.serializers import RechargeSerializer
from rest_framework import generics
from dandhacontrol.appviews import CustomObjectPermission



class RechargeListCreateView(generics.ListCreateAPIView):
    serializer_class = RechargeSerializer

    def get_queryset(self):
        client_id = self.request.client_id
        queryset = Recharge.objects.filter(device__customer__client__client_auth_id=client_id)

        # Filter by recharge date
        recharge_date = self.request.query_params.get('recharge_date', None)
        if recharge_date is not None:
            queryset = queryset.filter(device__recharge_date=recharge_date)

        # Filter by locality
        locality = self.request.query_params.get('locality', None)
        if locality is not None:
            queryset = queryset.filter(device__locality__area=locality)

        return queryset

class RechargeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recharge.objects.all()
    serializer_class = RechargeSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly, )
