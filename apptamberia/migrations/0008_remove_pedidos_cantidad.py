# Generated by Django 4.0.4 on 2022-06-26 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apptamberia', '0007_alter_pedidos_cantidad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedidos',
            name='cantidad',
        ),
    ]
