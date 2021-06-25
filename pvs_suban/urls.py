from rest_framework.routers import DefaultRouter
from .views import  ContactApiView, InvoiceApiView, AddressApiView, InvoicePositionApiView, CountryApiView

router = DefaultRouter()
router.register("contacts", ContactApiView)
router.register("invoices", InvoiceApiView)
router.register("addresses", AddressApiView)
router.register("invoicepositions", InvoicePositionApiView)
router.register("countries", CountryApiView)

urlpatterns = router.urls