from django.contrib import admin

from cartriges.models import Cartrige, Printer, UsablePrinters


admin.site.register(Cartrige)
admin.site.register(Printer)
admin.site.register(UsablePrinters)