
from django.forms import ModelForm

from operations.models import Operation


class OperationForm(ModelForm):
    class Meta:
        model = Operation
        fields = ['printer', 'item']