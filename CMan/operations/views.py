from django.db import transaction
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView
from django.views.generic.edit import DeleteView

from cartriges.models import Cartrige
from devices.models import UsablePrinter
from operations.models import Operation
from operations.forms import OperationForm


class OperationsListView(ListView):
    """Список всех операций, типа история."""

    model = Operation
    context_object_name = "operations"


class OperationsAddView(FormView):
    model = Operation
    form_class = OperationForm
    template_name = "operations/operation_add.html" 
    success_url = reverse_lazy("operations:index")
    
    def get_initial(self):
           initial = super().get_initial()
           inv_number = self.kwargs.get('inv_number')
           cartrige_slug = self.kwargs.get('cartrige_slug')

           if inv_number:
               initial['printer'] = UsablePrinter.objects.get(inv_number=inv_number)
           elif cartrige_slug:
               initial['item'] = Cartrige.objects.get(slug=cartrige_slug)

           return initial

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        inv_number = self.kwargs.get('inv_number')
        cartrige_slug = self.kwargs.get('cartrige_slug')
        
        if inv_number:
            usable_printers = UsablePrinter.objects.filter(inv_number=inv_number).prefetch_related('printer')
            compatible_cartridges = Cartrige.objects.filter(printer__in=usable_printers.values('printer'))
            form.fields['item'].queryset = compatible_cartridges

        elif cartrige_slug:
            compatible_printers = UsablePrinter.objects.filter(printer__cartrige__slug=cartrige_slug)
            form.fields['item'].queryset = compatible_printers
        
        return form


    def form_valid(self, form):
        with transaction.atomic():
            form.save()
            selected_cartrige = form.cleaned_data['item']

            if selected_cartrige.amount > 0:
                selected_cartrige.amount -= 1
                selected_cartrige.save()
            else:
                form.add_error('item', 'Недостаточно картриджей на складе.')
                return self.form_invalid(form)
        return super().form_valid(form)


class OperationsRemoveView(DeleteView):
    model = Operation
    pk_url_kwarg = "operation_id"
    context_object_name = "operation"
    success_url = reverse_lazy("operations:index")
    
    def post(self, request, *args, **kwargs):
        operation = self.get_object()

        with transaction.atomic():
            selected_cartrige = operation.item
            selected_cartrige.amount += 1
            selected_cartrige.save()

            operation.delete()
        return HttpResponseRedirect(self.success_url)