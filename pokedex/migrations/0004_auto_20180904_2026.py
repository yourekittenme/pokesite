# Generated by Django 2.1.1 on 2018-09-05 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0003_pokemon_weakness7'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='weight',
            field=models.DecimalField(decimal_places=1, max_digits=5),
        ),
    ]
