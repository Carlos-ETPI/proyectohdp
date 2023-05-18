from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import Empresa,Discapacidad
from django.urls import reverse_lazy
from .forms import EmpresaForm,DiscapacidadForm
from django.contrib import messages
# Create your views here.
def prueba(request):
    return render(request,'estadisticos/prueba.html')

class ListarDiscapacidad(ListView):
    template_name='estadisticos/listar-discapacidad.html'
    model=Discapacidad
    context_object_name='lista_discapacitado'
    queryset=Discapacidad.objects.all()
    
class CrearDiscapacidad(CreateView):
    template_name='estadisticos/crear-discapacidad.html'
    form_class=DiscapacidadForm
    success_url=reverse_lazy('estadisticos_app:listar-discapacidad')
    def form_valid(self, form):
        messages.success(self.request, 'La discapacidad se ha agregado exitosamente')
        return super().form_valid(form)
    
class EliminarDiscapacidad(DeleteView):
    template_name='estadisticos/eliminar-discapacidad.html'
    model=Discapacidad
    success_url=reverse_lazy('estadisticos_app:listar-discapacidad')
    def delete(self, request,*args, **kwargs):
        messages.success(request,'Discapacidad eliminada con exito')
        return super().delete(request,*args,**kwargs)
    
class ModificarDiscapacidad(UpdateView):
    template_name='estadisticos/modificar-discapacidad.html'
    model=Discapacidad
    form_class=DiscapacidadForm
    success_url=reverse_lazy('estadisticos_app:listar-discapacidad')
    def form_valid(self, form):
        messages.success(self.request, 'La discapacidad se ha modificado exitosamente')
        return super().form_valid(form)

class ListarEmpresa(ListView):
    template_name='estadisticos/listar-empresas.html'
    model=Empresa
    context_object_name='lista_empresas'
    queryset=Empresa.objects.all()
    
class CrearEmpresa(CreateView):
    template_name='estadisticos/crear-empresa.html'
    form_class=EmpresaForm
    success_url=reverse_lazy('estadisticos_app:listar-empresas')
    def form_valid(self, form):
        messages.success(self.request, 'La empresa se ha agregado exitosamente')
        return super().form_valid(form)