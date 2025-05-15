from django.forms import ModelForm

from devices.models import UsablePrinter

class UsablePrinterForm(ModelForm): #форма по изменению данных о конкретном принтере (перенос в другое помещение)
    class Meta:
        model = UsablePrinter
        fields = ""