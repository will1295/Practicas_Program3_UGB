# Generated by Django 4.1.2 on 2022-10-27 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_compras', '0002_delete_tblempleados_delete_tblproveedores_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tblProductos',
        ),
    ]
