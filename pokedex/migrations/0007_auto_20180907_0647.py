# Generated by Django 2.1.1 on 2018-09-07 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0006_auto_20180907_0644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True),
        ),
    ]
