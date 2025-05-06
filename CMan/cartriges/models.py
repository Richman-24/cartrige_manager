from django.db import models



class Printer(models.Model):
    name = models.CharField(max_length=256, unique=True, verbose_name="Модель")

    class Meta:
        db_table = "printers"
        verbose_name = "принтер"
        verbose_name_plural = "принтеры"
        ordering = ("name",)
    
    def __str__(self):
        return self.name


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
        ordering = ("name",)
    
    def __str__(self):
        return f"{self.name} | {self.amount} - {self.category}"