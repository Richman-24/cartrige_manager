from django.db import models

from buildings.models import Cabinet



class Printer(models.Model):
    name = models.CharField(max_length=256, unique=True, verbose_name="Модель")

    class Meta:
        db_table = "printers"
        verbose_name = "принтер"
        verbose_name_plural = "принтеры"
        ordering = ("name",)
    
    def __str__(self):
        return self.name


class UsablePrinters(models.Model):
    PRINTER_STATUS = {
        "working": "Исправен",
        "broken": "Сломан",
    }
    
    cabinet = models.ForeignKey(to=Cabinet, on_delete=models.PROTECT, verbose_name="кабинет")
    printer = models.ForeignKey(to=Printer, on_delete=models.PROTECT, verbose_name="принтер")
    inv_number = models.PositiveSmallIntegerField(unique=True, verbose_name="инвентаризационный номер")
    # serial_number = models.CharField(max_length=30, verbose_name="серийный номер")
    status = models.CharField(max_length=8, choices=PRINTER_STATUS, verbose_name="Состояние")
    comment = models.TextField(max_length=256, blank=True,  null=True, verbose_name="комментарий")

    class Meta:
        db_table="usable_printers"
        default_related_name="usable_printers"
        verbose_name="используемый принтер"
        verbose_name_plural="используемые принтеры"
        ordering=("cabinet__name",)

    def __str__(self):
        return f"{self.cabinet.name} | {self.printer.name} | {self.inv_number} "

class Cartrige(models.Model):
    CATEGORY_CHOICE = {
        "cartrige":"Картридж",
        "drum":"Барабан",
    }

    name = models.CharField(max_length=256, unique=True, verbose_name="Модель")
    slug = models.SlugField(max_length=256, unique=True, verbose_name="URL")
    amount = models.PositiveSmallIntegerField(default=0, verbose_name="Количество")
    printer = models.ManyToManyField(to=Printer, verbose_name="Совместимость")
    category = models.CharField(max_length=8, choices=CATEGORY_CHOICE, verbose_name="Тип расходника")

    class Meta:
        db_table = "cartriges"
        default_related_name = "cartriges"
        verbose_name = "картридж"
        verbose_name_plural = "картриджи"
        ordering = ("category", "name",)
    
    def __str__(self):
        return f"{self.name} | {self.amount} - {self.category}"
