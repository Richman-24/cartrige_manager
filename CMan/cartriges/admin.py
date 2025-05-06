from django.contrib import admin

from cartriges.models import Cartrige


@admin.register(Cartrige)
class CartrigeAdmin(admin.ModelAdmin):
    list_display=("name","amount","category")
    list_editable=("amount",)
    prepopulated_fields = {"slug": ("name",)}

