from django.shortcuts import render
from django.views.generic import ListView, DetailView

from cartriges.models import Cartrige

class CartrigesListView(ListView):
    model = Cartrige
    context_object_name = "cartriges"

class CartrigeDetailView(DetailView):
    template_name = "cartriges/cartrige_detail.html"
    context_object_name = "cartrige"
    slug_url_kwarg="cartrige_slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['printers'] = self.object.printer.all()
        return context

    def get_queryset(self):
        return Cartrige.objects.prefetch_related('printer')
