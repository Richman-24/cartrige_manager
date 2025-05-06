from django.db import models

from cartriges.models import Cartrige
from devices.models import UsablePrinter

class Supports(models.Model):
    # user = ...
    printer = models.ForeignKey(to=UsablePrinter, on_delete=models.PROTECT, verbose_name="принтер")
    item = models.ForeignKey(to=Cartrige, on_delete=models.PROTECT, verbose_name="расходник")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата замены")

    class Meta:
        db_table = "supports"
        verbose_name="обслуживание"
        verbose_name_plural="обслуживание"
    
    def __str__(self):
        return f"{self.created_at} - {self.printer.cabinet.name} | {self.printer.printer.name}"
