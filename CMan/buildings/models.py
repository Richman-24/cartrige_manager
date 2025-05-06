from django.db import models


class Cabinet(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name="Номер кабинета")

    class Meta:
        db_table = "cabinet"
        verbose_name = "кабинет"
        verbose_name_plural = "кабинеты"
        ordering = ("name",)
    
    def __str__(self):
        return f"{self.name}"