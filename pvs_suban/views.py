from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import ContactSerializer, InvoiceSerializer, AddressSerializer, InvoicePositionSerializer, CountrySerializer
from .models import Contact, Invoice, Address, InvoicePosition, Country
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ContactApiView(ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type']
    pagination_class = None
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'delete']

class InvoiceApiView(ModelViewSet):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['address__contact__name']
    ordering_fields = ['id'] #noch ein bisschen Ordering, nur für mich um es zu lernen
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'delete']

class AddressApiView(ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'delete']

class InvoicePositionApiView(ModelViewSet):
    serializer_class = InvoicePositionSerializer
    queryset = InvoicePosition.objects.all()
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'delete']

class CountryApiView(ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['value']
    pagination_class = None
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']