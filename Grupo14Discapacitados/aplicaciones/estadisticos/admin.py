from django.contrib import admin
from .models import Empresa,Censo,Discapacidad

# Register your models here.
class EmpresaAdmin(admin.ModelAdmin):
    list_display=('idempresa','nombre_empresa','total_personas','censo')
    search_fields=('nombre_empresa',)
    
admin.site.register(Empresa,EmpresaAdmin)
admin.site.register(Censo)
admin.site.register(Discapacidad)