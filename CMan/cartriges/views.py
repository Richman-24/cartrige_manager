from django.db.models import Prefetch
from django.views.generic import ListView, DetailView


from cartriges.models import Cartrige
from devices.models import UsablePrinter


class CartrigesListView(ListView):
    model = Cartrige
    context_object_name = "cartriges"


class CartrigeDetailView(DetailView):
    model = Cartrige
    context_object_name = "cartrige"
    slug_url_kwarg="cartrige_slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        printers = self.object.printer.all()
        # printers = self.object.printer.prefetch_related(  # Проверить на большой базе = сколько их будет дальше
        #     'usableprinter_set__cabinet'
        # )
        usable_printers = UsablePrinter.objects.filter(printer_id__in=printers)

        context['devices'] = usable_printers

        return context
