from django.urls import path

from cartriges.views import CartrigesListView, CartrigeDetailView, PrinterDetailView, PrinterListView

app_name="cartriges"


urlpatterns = [
    path('cartriges/', CartrigesListView.as_view(), name="index"),
    path('cartriges/<slug:cartrige_slug>', CartrigeDetailView.as_view(), name="detail"),
    path('printers/', PrinterListView.as_view(), name="printers"),
    path('printers/<int:printer_pk>', PrinterDetailView.as_view(), name="printers"),
    #тут будет ссылка на принтер по inv_number
    #path('usable-printers/<int:inv_number>', UsablePrinterDetailView.as_view(), name="usable-printers"),


    


]