# import APIView as APIView
from rest_framework import generics
from rest_framework import status, filters
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CategorySerializer, DonationSerializer, CitySerializer, AppealSerializer
from .models import Donation, Category, City, Appeal
from rest_framework.decorators import api_view
from rest_framework import viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend


class CategoryAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryDetail(generics.RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class DonationAPIView(generics.ListCreateAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['categoryId', 'city']


class DonationDetail(generics.RetrieveAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer


class CityListAPIView(generics.ListAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()


class AppealListAPIView(generics.ListCreateAPIView):
    serializer_class = AppealSerializer
    queryset = Appeal.objects.all()






