# Generated by Django 3.2.13 on 2022-11-09 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('idEstado', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idEstado')),
                ('nombre', models.CharField(max_length=25)),
                ('ISO', models.CharField(blank=True, max_length=3, null=True)),
            ],
            options={
                'db_table': 'Estado',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('idPais', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idPais')),
                ('nombre', models.CharField(max_length=45)),
                ('ISO', models.CharField(max_length=2)),
                ('codNumIso', models.IntegerField(blank=True, null=True)),
                ('formDirec', models.CharField(blank=True, max_length=80, null=True)),
            ],
            options={
                'db_table': 'Pais',
            },
        ),
        migrations.CreateModel(
            name='Mundeleg',
            fields=[
                ('idMunDeleg', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idMunDeleg')),
                ('nombre', models.CharField(max_length=45)),
                ('fk_Estado', models.ForeignKey(blank=True, db_column='fk_Estado', null=True, on_delete=django.db.models.deletion.SET_NULL, to='datosgeograficos.estado', verbose_name='Estado')),
            ],
            options={
                'db_table': 'MunDeleg',
            },
        ),
        migrations.AddField(
            model_name='estado',
            name='fk_Pais',
            field=models.ForeignKey(db_column='fk_Pais', on_delete=django.db.models.deletion.CASCADE, to='datosgeograficos.pais', verbose_name='País'),
        ),
        migrations.CreateModel(
            name='CP',
            fields=[
                ('cp', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='cp')),
                ('fk_MunDeleg', models.ForeignKey(blank=True, db_column='fk_MunDeleg', null=True, on_delete=django.db.models.deletion.SET_NULL, to='datosgeograficos.mundeleg', verbose_name='Municipio')),
            ],
            options={
                'db_table': 'CP',
            },
        ),
    ]