# Generated by Django 4.1.2 on 2022-10-27 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_compras', '0004_tblempleados_tblproveedores_tblsucursales'),
    ]

    operations = [
        migrations.CreateModel(
            name='tblProductos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('existencia', models.CharField(max_length=200)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_compras.tblproveedores')),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_compras.tblsucursales')),
            ],
        ),
    ]
