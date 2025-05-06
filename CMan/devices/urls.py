from django.urls import path

from devices.views import PrinterDetailView, PrinterListView

app_name="devices"


urlpatterns = [

    path('', PrinterListView.as_view(), name="printers"),
    path('<int:printer_pk>', PrinterDetailView.as_view(), name="printer"),
    #тут будет ссылка на принтер по inv_number
    #path('usable-printers/<int:inv_number>', UsablePrinterDetailView.as_view(), name="usable-printers"),
]