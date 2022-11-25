# Generated by Django 3.2.13 on 2022-11-09 23:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datosgeograficos', '0001_initial'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('idCargo', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idCargo')),
                ('nombre', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'Cargo',
            },
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('idContrato', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idContrato')),
                ('tipo', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'Contrato',
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('idDepto', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idDepto')),
                ('nombre', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'Departamento',
            },
        ),
        migrations.CreateModel(
            name='HistorialUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id')),
                ('usuario', models.CharField(max_length=45)),
                ('entidad', models.CharField(max_length=45)),
                ('modulo', models.CharField(max_length=45)),
                ('movimiento', models.CharField(max_length=45)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('observaciones', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'HistorialUsuario',
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('idEmpleado', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idEmpleado')),
                ('fechaNac', models.DateField(blank=True, null=True)),
                ('lugarNac', models.CharField(blank=True, max_length=45, null=True)),
                ('RFC', models.CharField(blank=True, max_length=13, null=True)),
                ('CURP', models.CharField(blank=True, max_length=18, null=True)),
                ('celular', models.CharField(blank=True, max_length=12, null=True)),
                ('calle', models.CharField(blank=True, max_length=45, null=True)),
                ('noInt', models.IntegerField(blank=True, null=True)),
                ('noExt', models.IntegerField(blank=True, null=True)),
                ('fk_CP', models.ForeignKey(blank=True, db_column='fk_CP', null=True, on_delete=django.db.models.deletion.CASCADE, to='datosgeograficos.cp', verbose_name='Código Postal')),
                ('fk_User', models.ForeignKey(db_column='fk_User', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'db_table': 'Empleado',
            },
        ),
        migrations.CreateModel(
            name='DatosLaborales',
            fields=[
                ('idDatosLab', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idDatosLab')),
                ('codigo', models.CharField(max_length=5)),
                ('fechaIng', models.DateField()),
                ('fechaBaja', models.DateField(blank=True, null=True)),
                ('sueldoMensual', models.FloatField(blank=True, null=True)),
                ('referencia1', models.CharField(blank=True, max_length=200, null=True)),
                ('referencia2', models.CharField(blank=True, max_length=200, null=True)),
                ('ubicacion', models.CharField(blank=True, max_length=45, null=True)),
                ('procedencia', models.CharField(blank=True, max_length=10, null=True)),
                ('observaciones', models.CharField(blank=True, max_length=250, null=True)),
                ('fk_Cargo', models.ForeignKey(db_column='fk_Cargo', on_delete=django.db.models.deletion.CASCADE, to='usuarios.cargo', verbose_name='Cargo')),
                ('fk_Contrato', models.ForeignKey(db_column='fk_Contrato', on_delete=django.db.models.deletion.CASCADE, to='usuarios.contrato', verbose_name='Contrato')),
                ('fk_Empleado', models.ForeignKey(db_column='fk_Empleado', on_delete=django.db.models.deletion.CASCADE, to='usuarios.empleado', verbose_name='Empleado')),
            ],
            options={
                'db_table': 'DatosLaborales',
            },
        ),
        migrations.AddField(
            model_name='cargo',
            name='fk_Depto',
            field=models.ForeignKey(db_column='fk_Depto', on_delete=django.db.models.deletion.CASCADE, to='usuarios.departamento', verbose_name='Departamento'),
        ),
    ]