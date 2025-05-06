from django.views.generic import ListView

from buildings.models import Cabinet


class CampusListView(ListView):
    model = Cabinet
    context_object_name = "cabinets"

