from django import forms
from django.forms import ModelForm
from .models import Empresa,Discapacidad
from django.core.exceptions import ValidationError

        
GENDER_CHOICES = (
    ('Masculino ', 'Masculino'),
    ('Femenino', 'Femenino'),
    
)
LOCALIZACION_CHOICES = (
        ('Urbano', 'Urbana'),
        ('Rural', 'Rural'),
    )
DISCAPACIDAD_CHOICES1 = (
        ('Visual', 'Discapacidad Visual'),
        ('Fisica', 'Discapacidad Fisica'),
        ('Comunicacion', 'Discapacidad de Comunicacion'),
        ('Auditiva', 'Discapacidad Auditiva'),
        ('intelectual', 'Discapacidad intelectual'),
        ('social', 'Discapacidad Psicosocial o Mental'),
        ('Dependencia', 'Discapacidad por Dependencia'),
    )
class DiscapacidadForm(forms.ModelForm):
    sexo = forms.ChoiceField(choices=GENDER_CHOICES, label="Sexo")
    localizacion = forms.ChoiceField(choices=LOCALIZACION_CHOICES, label="Localizacion")
    tipo_discapacidad = forms.ChoiceField(choices=DISCAPACIDAD_CHOICES1, label="Discapacidad")
    class Meta:
        model = Discapacidad
        fields = ['tipo_discapacidad','sexo','localizacion','total_personas','censo']
    

class EmpresaForm(ModelForm):
    
    sexo = forms.ChoiceField(choices=GENDER_CHOICES, label="Sexo")
    localizacion = forms.ChoiceField(choices=LOCALIZACION_CHOICES, label="Localizacion")
    tipo_discapacidad = forms.ChoiceField(choices=DISCAPACIDAD_CHOICES1, label="Discapacidad")
    class Meta:
        model = Empresa
        fields = ['nombre_empresa','sexo','localizacion','tipo_discapacidad','total_personas','censo']

    