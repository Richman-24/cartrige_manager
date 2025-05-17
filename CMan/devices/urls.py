from django.urls import path

from devices.views import PrinterListView, UsablePrinterDetailView, UsablePrinterEditView

app_name="devices"


urlpatterns = [

    path('', PrinterListView.as_view(), name="printers"),
    path('use/<int:inv_number>/', UsablePrinterDetailView.as_view(), name="usable_printers"),
    path('use/<int:inv_number>/edit/', UsablePrinterEditView.as_view(), name="usable_printers_edit"),
]