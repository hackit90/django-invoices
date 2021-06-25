from django.db import models
from django.db.models import Sum, ForeignKey
from django.db.models import F
from django.core.validators import EmailValidator

# Create your models here.
class Contact(models.Model):
    TYPE_SELECTpriv = (
        ('private', 'Private'),
        ('company', 'Company'),
    )
# Ich weiss, dass die Aufgabe nur ein Charfield möchte, aber hab da einfach mal weitergedacht^^
    TYPE_SELECTsalut = (
        ('herr', 'Herr'),
        ('frau', 'Frau'),
        ('familie', 'Familie'),
        ('andere', 'Andere'),
    )
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=30, choices=TYPE_SELECTpriv, default='private')
    salutation = models.CharField(max_length=30, choices=TYPE_SELECTsalut, default='frau')
    name = models.CharField(max_length=256, blank=False, default='Vor- und Nachname')
    email = models.EmailField(max_length=256, blank=False, validators=[EmailValidator])

    def __str__(self):
        return self.name

class Address(models.Model):
    id = models.AutoField(primary_key=True)
    street = models.CharField(max_length=256, blank=True)
    zip = models.CharField(max_length=10, blank=False)
    city = models.CharField(max_length=256, blank=False)
    country = models.ForeignKey('Country',on_delete=models.CASCADE, related_name='countries', null=True)
    contact = models.ForeignKey('Contact', on_delete=models.CASCADE, related_name='addresses')

    def __str__(self):
        return '%s, %s, %s' % (self.street, self.zip, self.city)


class Country(models.Model):
    key = models.CharField(max_length=20, primary_key=True)
    value = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return '%s, %s' % (self.key, self.value)


class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256, blank=False)
    body = models.TextField(max_length=512, blank=False, default='payload')
    condition = models.CharField(max_length=256, blank=True, null=True)
    due = models.DateField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    address = models.ForeignKey('Address', on_delete=models.CASCADE, related_name='invoices', blank=True, null=True)

    def total(self):
        totalAmount = InvoicePosition.objects.filter(invoice=self.id).aggregate(sum=Sum(F('amount') * F('quantity')))[
            'sum']
        return totalAmount

    def __str__(self):
        return '%s, %s %s %s %s' % (self.title, self.due, self.date, self.total(), self.address)

class InvoicePosition(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256, blank=False)
    body = models.TextField(blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    amount = models.FloatField(max_length=50, blank=True, null=True, default=0.00)
    invoice = models.ForeignKey('Invoice', on_delete=models.CASCADE, related_name='InvoicePositions', blank=True,
                                null=True)