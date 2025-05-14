from django.views.generic import ListView, DetailView

from cartriges.models import Printer
from devices.models import UsablePrinter


class PrinterListView(ListView):
    model=Printer
    context_object_name = "printers"


class PrinterDetailView(DetailView): # передумать, переделать!
    context_object_name = "printer"
    pk_url_kwarg = "printer_pk"

    def get_queryset(self):
        return Printer.objects.prefetch_related('cartriges', 'usable_printers')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cartriges'] = self.object.cartriges.all()
        context['devices'] = self.object.usable_printers.all()
        context['devices'] = self.object.usable_printers.all()
        return context



class UsablePrinterDetailView(DetailView):
    context_object_name = "device"
    pk_url_kwarg = "inv_number"

    def get_object(self, queryset = None):
        return UsablePrinter.objects.get(
            inv_number=self.kwargs.get(self.pk_url_kwarg)
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cartriges'] = self.get_object().printer.cartriges.all()
        return context