from django.contrib import admin

from devices.models import Printer, UsablePrinter


admin.site.register(Printer)
admin.site.register(UsablePrinter)