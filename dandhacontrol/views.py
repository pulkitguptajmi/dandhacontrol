from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import filters
from rest_framework import viewsets
from .models import Company, CompanyServiceRelationship
from .serializers import CompanySerializer, CompanyServiceRelationshipSerializer

from rest_framework import permissions

class CustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return True


# class ExampleView(RetrieveUpdateDestroyAPIView):
#     permission_classes = (CustomPermission,)


#
#
# class Company(generics.):
#     queryset = AirportInfo.objects.all()
#     serializer_class = AirportInfoSerializer
#     filter_backends = [filters.SearchFilter]
#     filterset_fields = ['nameairport']
#



#
#
# class Company(generics.):
#     queryset = AirportInfo.objects.all()
#     serializer_class = AirportInfoSerializer
#     filter_backends = [filters.SearchFilter]
#     filterset_fields = ['nameairport']
#
#
# class AirportList(generics.ListAPIView):
#     queryset = AirportInfo.objects.all()
#     serializer_class = AirportInfoSerializer
#     filter_backends = [filters.SearchFilter]
#     filterset_fields = ['nameairport']
#
# class AirportExistView(generics.ListAPIView):
#     queryset = AirportInfo.objects.all()
#     serializer_class = AirportExistSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['codeiataairport']
#
# class GiftList(generics.ListAPIView):
#     queryset = GiftInfo.objects.all()
#     serializer_class = GiftInfoSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['airport__codeiataairport', 'for_him', 'for_her', 'for_kids']
#
# class ShoppingList(generics.ListAPIView):
#     queryset = GiftInfo.objects.all()
#     serializer_class = GiftInfoSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['airport__codeiataairport']
#
#     def get_queryset(self):
#         # gift_ids = self.queryset.values_list('shop_name', flat=True).distinct()
#         queryset = self.queryset.distinct('shop_name')
#         return queryset
#
# class FoodList(generics.ListAPIView):
#     queryset = FoodInfo.objects.all()
#     serializer_class = FoodInfoSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['airport__codeiataairport']
#
# class SpaList(generics.ListAPIView):
#     queryset = SpaInfo.objects.all()
#     serializer_class = SpaInfoSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['airport__codeiataairport']
#
# class LoungeList(generics.ListAPIView):
#     queryset = LoungesInfo.objects.all()
#     serializer_class = LoungesInfoSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['airport__codeiataairport']