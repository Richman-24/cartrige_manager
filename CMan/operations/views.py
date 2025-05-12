from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from operations.models import Operation
from operations.forms import OperationAddForm


class OperationsListView(ListView):
    """Список всех операций, типа история."""

    model = Operation
    context_object_name = "operations"


class OperationsAddView(FormView):
    model = Operation
    form_class = OperationAddForm
    template_name = "operations/operation_add.html" 
    success_url = reverse_lazy("operations:index")

    def form_valid(self, form):
        # Начинаем атомарную транзакцию
        with transaction.atomic():
            # Сохраняем объект операции
            operation = form.save()
            
            # Получаем выбранный картридж из формы
            selected_cartrige = form.cleaned_data['item']
            
            # Уменьшаем количество картриджа на 1
            if selected_cartrige.amount > 0:
                selected_cartrige.amount -= 1
                selected_cartrige.save()
            else:
                form.add_error('item', 'Недостаточно картриджей на складе.')
                return self.form_invalid(form)

        return super().form_valid(form)

class OperationsEditView(FormView): ...

class OperationsRemoveView(FormView): ...
