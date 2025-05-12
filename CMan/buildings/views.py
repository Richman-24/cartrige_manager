from django.http import Http404
from django.views.generic import ListView, DetailView

from buildings.models import Cabinet
from devices.models import UsablePrinter


class CampusListView(ListView):
    model = Cabinet
    context_object_name = "cabinets"


class CampusCabinetView(DetailView):
    model = Cabinet
    template_name = "buildings/cabinet_detail.html"
    pk_url_kwarg = "cabinet_pk"
    context_object_name = "devices"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cabinet_pk = self.kwargs.get(self.pk_url_kwarg)
        context["devices"] = (
            UsablePrinter.objects.select_related()
            .filter(cabinet_id=cabinet_pk)
        )
        
        return context