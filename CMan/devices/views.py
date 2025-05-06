from django.views.generic import ListView, DetailView

from cartriges.models import Printer


class PrinterListView(ListView):
    model=Printer
    context_object_name = "printers"


class PrinterDetailView(DetailView):
    context_object_name = "printer"
    pk_url_kwarg = "printer_pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cartriges'] = self.object.cartriges.all()
        return context

    def get_queryset(self):
        return Printer.objects.prefetch_related('cartriges')

