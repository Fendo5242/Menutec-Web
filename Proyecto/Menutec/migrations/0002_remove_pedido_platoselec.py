# Generated by Django 4.2.3 on 2023-07-10 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Menutec', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='platoselec',
        ),
    ]
