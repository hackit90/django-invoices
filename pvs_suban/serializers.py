from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Contact, InvoicePosition, Address, Invoice, Country

#Adresse integrieren
class AddressNestedSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = ['street', 'zip', 'city', 'country', 'id']
class ContactSerializer(ModelSerializer):
    addresses = AddressNestedSerializer(many=True)
    class Meta:
        model = Contact
        fields = ['type', 'salutation', 'name', 'email','addresses', 'id']
        read_only_fields = ['addresses']

#InvoicePosition integrieren
class InvoicePositionNestedSerializer(ModelSerializer):
    class Meta:
        model = InvoicePosition
        fields = '__all__'
class InvoiceSerializer(ModelSerializer):
     InvoicePositions = InvoicePositionNestedSerializer(many=True)
     total_amount = serializers.FloatField(source='total')

     class Meta:
         model = Invoice
         fields = ['title', 'body', 'date', 'due', 'condition', 'InvoicePositions', 'total_amount', 'id']
         read_only_fields = ['InvoicePositions']

class InvoicePositionSerializer(ModelSerializer):
    class Meta:
        model = InvoicePosition
        fields = '__all__'
    total = serializers.SerializerMethodField()
    def get_total(self, obj):
        return obj.quantity * obj.amount

class AddressSerializer(ModelSerializer):
    country_name = serializers.SerializerMethodField(source='get_country_name')
    contact = serializers.SerializerMethodField(source='get_contact')
    class Meta:
        model = Address
        fields = ['street', 'zip', 'city', 'invoices', 'contact', 'country_name', 'id']
    def get_country_name(self, obj):
        return obj.country.value
    def get_contact(self, obj):
        return obj.contact.name

class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'