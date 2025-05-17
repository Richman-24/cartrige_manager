from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView

from cartriges.models import Printer
from devices.models import UsablePrinter


class PrinterListView(ListView):
    model=UsablePrinter
    context_object_name = "printers"


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


class UsablePrinterEditView(UpdateView):
    model = UsablePrinter
    fields = '__all__'
    success_url = reverse_lazy("devices:usable_printers")