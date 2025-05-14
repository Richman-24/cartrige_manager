from django.urls import path

from devices.views import PrinterDetailView, PrinterListView, UsablePrinterDetailView

app_name="devices"


urlpatterns = [

    path('', PrinterListView.as_view(), name="printers"),
    path('<int:printer_pk>', PrinterDetailView.as_view(), name="printer"),
    path('use/<int:inv_number>/', UsablePrinterDetailView.as_view(), name="usable_printers"),
]