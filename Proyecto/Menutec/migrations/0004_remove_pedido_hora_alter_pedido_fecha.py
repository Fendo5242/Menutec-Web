# Generated by Django 4.2.2 on 2023-07-10 20:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menutec', '0003_pedido_hora'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='hora',
        ),
        migrations.AlterField(
            model_name='pedido',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
