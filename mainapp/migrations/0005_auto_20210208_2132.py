# Generated by Django 3.0.7 on 2021-02-08 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20210204_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='phone_num',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
