# Generated by Django 4.2.7 on 2023-11-27 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='data',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='valor_total',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
    ]
