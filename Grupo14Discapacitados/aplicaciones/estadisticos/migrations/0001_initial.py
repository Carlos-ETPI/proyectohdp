# Generated by Django 3.2.19 on 2023-05-16 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Censo',
            fields=[
                ('idcenso', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre_censo', models.CharField(max_length=255)),
                ('fecha', models.DateField()),
                ('activo', models.BooleanField(verbose_name='Activo')),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('idempresa', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre_empresa', models.CharField(max_length=255)),
                ('sexo', models.CharField(default='', max_length=13, verbose_name=(('Masculino', 'Masculino'), ('Femenino', 'Femenino')))),
                ('localizacion', models.CharField(default='', max_length=13, verbose_name=(('Urbana', 'Urbana'), ('Rural', 'Rural')))),
                ('tipo_discapacidad', models.CharField(default='', max_length=13, verbose_name=(('Visual', 'Discapacidad Visual'), ('Fisica', 'Discapacidad Fisica'), ('Comunicacion', 'Discapacidad de Comunicacion'), ('Auditiva', 'Discapacidad Auditiva'), ('intelectual', 'Discapacidad intelectual'), ('social', 'Discapacidad Psicosocial o Mental'), ('Dependencia', 'Discapacidad por Dependencia')))),
                ('total_personas', models.PositiveIntegerField()),
                ('censo', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='empresa_censo', to='estadisticos.censo')),
            ],
        ),
        migrations.CreateModel(
            name='Discapacidad',
            fields=[
                ('id_discapacidad', models.BigAutoField(primary_key=True, serialize=False)),
                ('sexo', models.CharField(default='', max_length=13, verbose_name=(('M', 'Masculino'), ('F', 'Femenino')))),
                ('localizacion', models.CharField(default='', max_length=13, verbose_name=(('U', 'Urbana'), ('R', 'Rural')))),
                ('tipo_discapacidad', models.CharField(default='', max_length=13, verbose_name=(('Visual', 'Discapacidad Visual'), ('Fisica', 'Discapacidad Fisica'), ('Comunicacion', 'Discapacidad de Comunicacion'), ('Auditiva', 'Discapacidad Auditiva'), ('intelectual', 'Discapacidad intelectual'), ('social', 'Discapacidad Psicosocial o Mental'), ('Dependencia', 'Discapacidad por Dependencia')))),
                ('total_personas', models.PositiveIntegerField()),
                ('censo', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='discapacidades_censo', to='estadisticos.censo')),
            ],
        ),
    ]
