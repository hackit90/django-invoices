from django.contrib import admin
from django.urls import reverse
from django.db.models import Count

from .models import Contact, Address, Country, Invoice, InvoicePosition
# Register your models here.

class AddressInline(admin.StackedInline):
    model = Address
    extra = 0
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    inlines = [AddressInline]
    list_display = ['name', 'type', 'address_count']
    search_fields = ['name']
    list_filter = ['type']

    def address_count(self, obj):
        count = obj.addresses.count()
        return count

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['key', 'value']
    search_fields = ['value', 'key']

class InvoposInline(admin.StackedInline):
    model = InvoicePosition
    extra = 0
@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'date','due', 'total', 'contact_name']
    inlines = [InvoposInline]
    search_fields = ['title', 'address__contact__name']

    def contact_name(self, obj):
        return obj.address.contact.name
    contact_name.short_description = 'contact name'