from django.contrib import admin
from .models import Empresa,Censo,Discapacidad, Localidad, TipoLocalidad, Zona

# Register your models here.
class EmpresaAdmin(admin.ModelAdmin):
    list_display=('idempresa','nombre_empresa','total_personas','censo')
    search_fields=('nombre_empresa',)


class CensoAdmin(admin.ModelAdmin):
    list_display=('idcenso','nombre_censo',)
    search_fields=('nombre_censo',)

class LocaliadadAdmin(admin.ModelAdmin):
    list_display=('idlocalidad','nombre',)
    search_fields=('nombre',)


class ZonaAdmin(admin.ModelAdmin):
    list_display=('idzona','localidad','censo',)
    search_fields=('censo',)


class TipoLocalidaAdmin(admin.ModelAdmin,):
    list_display=('idtipo','nombre')
    search_fields=('nombre',)


admin.site.register(Empresa,EmpresaAdmin)
admin.site.register(Censo,CensoAdmin)
admin.site.register(Discapacidad)
admin.site.register(Zona,ZonaAdmin)
admin.site.register(TipoLocalidad,TipoLocalidaAdmin)
admin.site.register(Localidad,LocaliadadAdmin)