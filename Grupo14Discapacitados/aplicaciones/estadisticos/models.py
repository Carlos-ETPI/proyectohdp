from django.db import models

# Create your models here.
class Censo(models.Model):
    idcenso=models.BigAutoField(primary_key=True)
    nombre_censo=models.CharField(max_length=255)
    discapacidad=models.CharField(max_length=255,default="")
    isGeneral=models.BooleanField(default=False)
    fecha = models.DateField()
    activo=models.BooleanField('Activo')
    def __str__(self):
        return self.nombre_censo


class Zona(models.Model):
    idzona=models.BigAutoField(primary_key=True)
    censo=models.ForeignKey(Censo,on_delete=models.CASCADE)
    cantmujeres=models.IntegerField()
    cantHombres=models.IntegerField()
    localidad=models.ForeignKey('Localidad',on_delete=models.CASCADE)
    

class Localidad(models.Model):
    idlocalidad=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    isUrbano=models.BooleanField()
    tipo=models.ForeignKey('TipoLocalidad',on_delete=models.CASCADE)


class TipoLocalidad(models.Model):
    idtipo=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=50)



class Discapacidad(models.Model):
    id_discapacidad=models.BigAutoField(primary_key=True)
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    sexo=models.CharField( GENDER_CHOICES,max_length=13,default='')
    LOCALIZACION_CHOICES = (
        ('U', 'Urbana'),
        ('R', 'Rural'),
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
    DISCAPACIDAD_CHOICES = (
        ('Visual', 'Discapacidad Visual'),
        ('Fisica', 'Discapacidad Fisica'),
        ('Comunicacion', 'Discapacidad de Comunicacion'),
        ('Auditiva', 'Discapacidad Auditiva'),
        ('intelectual', 'Discapacidad intelectual'),
        ('social', 'Discapacidad Psicosocial o Mental'),
        ('Dependencia', 'Discapacidad por Dependencia'),
    )
    localizacion=models.CharField( LOCALIZACION_CHOICES,max_length=13,default='')
    tipo_discapacidad=models.CharField( DISCAPACIDAD_CHOICES1,max_length=13,default='')
    total_personas = models.PositiveIntegerField()
    censo = models.ForeignKey(Censo, on_delete=models.RESTRICT, related_name='discapacidades_censo')
    def __str__(self):
        return self.nombre_discapacidad
     
class Empresa(models.Model):
    idempresa=models.BigAutoField(primary_key=True)
    nombre_empresa = models.CharField(max_length=255)
    GENDER_CHOICES = (
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
    )
    sexo=models.CharField( GENDER_CHOICES,max_length=13,default='')
    LOCALIZACION_CHOICES = (
        ('Urbana', 'Urbana'),
        ('Rural', 'Rural'),
    )
    DISCAPACIDAD_CHOICES = (
        ('Visual', 'Discapacidad Visual'),
        ('Fisica', 'Discapacidad Fisica'),
        ('Comunicacion', 'Discapacidad de Comunicacion'),
        ('Auditiva', 'Discapacidad Auditiva'),
        ('intelectual', 'Discapacidad intelectual'),
        ('social', 'Discapacidad Psicosocial o Mental'),
        ('Dependencia', 'Discapacidad por Dependencia'),
    )
    localizacion=models.CharField( LOCALIZACION_CHOICES,max_length=13,default='')
    tipo_discapacidad=models.CharField( DISCAPACIDAD_CHOICES,max_length=13,default='')
    total_personas = models.PositiveIntegerField()
    censo = models.ForeignKey(Censo, on_delete=models.RESTRICT, related_name='empresa_censo')
    
    def __str__(self):
        return self.nombre_empresa
    