from django.db import models

from campus.models import Cabinet


class Printer(models.Model):
    name = models.CharField(max_length=256, unique=True, verbose_name="Модель")
    
    class Meta:
        db_table = "printers"
        verbose_name = "принтер"
        verbose_name_plural = "принтеры"
        ordering = ("name",)
    
    def __str__(self):
        return self.name


class UsablePrinter(models.Model):
    PRINTER_STATUS = {
        "working": "Исправен",
        "broken": "Сломан",
    }
    
    cabinet = models.ForeignKey(to=Cabinet, on_delete=models.PROTECT, verbose_name="кабинет")
    printer = models.ForeignKey(to=Printer, on_delete=models.PROTECT, verbose_name="принтер")
    inv_number = models.PositiveSmallIntegerField(unique=True, verbose_name="инвентаризационный номер")
    serial_number = models.CharField(max_length=30, unique=True, blank=True, null=True, verbose_name="серийный номер")
    status = models.CharField(max_length=8, choices=PRINTER_STATUS, verbose_name="Состояние")
    comment = models.TextField(max_length=256, blank=True,  null=True, verbose_name="комментарий")

    ip_adress = models.CharField(max_length=15, unique=True, blank=True, null=True, verbose_name="IP адрес устройства")# create validators 
    host_name = models.CharField(max_length=10, blank=True, null=True, verbose_name="Имя хоста в сети") 

    class Meta:
        db_table="usable_printers"
        default_related_name="usable_printers"
        verbose_name="используемый принтер"
        verbose_name_plural="используемые принтеры"
        ordering=("cabinet__name",)

    def __str__(self):
        return f"{self.cabinet.name} | {self.printer.name} | {self.inv_number} "
