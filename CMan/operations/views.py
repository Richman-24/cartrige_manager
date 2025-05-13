from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView
from django.views.generic.edit import DeleteView

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
        return super().delete(request, *args, **kwargs)