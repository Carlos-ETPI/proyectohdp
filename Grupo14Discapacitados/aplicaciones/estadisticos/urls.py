from django.urls import path
from . import views
import aplicaciones.estadisticos.views 
app_name='estadisticos_app'
urlpatterns = [
    path('estadisticos/prueba/',views.prueba,name='prueba'),
    path('estadisticos/listar-empresas/',views.ListarEmpresa.as_view(),name='listar-empresas'),
    path('estadisticos/crear-empresa/',views.CrearEmpresa.as_view(),name='crear-empresa'),
    path('estadisticos/listar-discapacidad/',views.ListarDiscapacidad.as_view(),name='listar-discapacidad'),
    path('estadisticos/crear-discapacidad/',views.CrearDiscapacidad.as_view(),name='crear-discapacidad'),
    path('estadisticos/eliminar-discapacidad/<pk>/',views.EliminarDiscapacidad.as_view(),name='eliminar-discapacidad'),
    path('estadisticos/modificar-discapacidad/<pk>/',views.ModificarDiscapacidad.as_view(),name='modificar-discapacidad'),
    path('estadisticos/generales',views.estadisticas,name="estadisticas generales"),
    path('estadisticos/getcenso/<id>',views.getCenso,name="estadisticas generales"),
    path('estadisticos/vergrafica/<id>',views.verGrafica,name="estadisticas individuales"),
    path('estadisticos/getgenerales',views.getGenerales,name="estadisticas generales"),
]
