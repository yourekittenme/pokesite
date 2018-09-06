# Generated by Django 2.1.1 on 2018-09-06 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0004_auto_20180904_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='icon',
            field=models.ImageField(default='None', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(default='None', upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='category',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='description',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='height',
            field=models.CharField(max_length=7),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='overgrow',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='type1',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='type2',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='weakness1',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='weakness2',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='weakness3',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='weakness4',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='weakness5',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='weakness6',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='weakness7',
            field=models.CharField(max_length=20),
        ),
    ]
