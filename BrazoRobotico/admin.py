from django.contrib import admin

from BrazoRobotico.models import Estado, Brazo, Movimiento, Posicion, PlacaControladora, ModuloBluetooth

# Register your models here.
admin.site.register(Estado)
admin.site.register(Brazo)
admin.site.register(Movimiento)
admin.site.register(Posicion)
admin.site.register(PlacaControladora)
admin.site.register(ModuloBluetooth)
