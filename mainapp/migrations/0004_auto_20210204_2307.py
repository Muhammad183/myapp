# Generated by Django 3.0.7 on 2021-02-04 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20210204_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
