# Generated by Django 2.0.5 on 2018-08-01 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finalapp', '0002_auto_20180728_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='C_amount_paid',
            field=models.CharField(default=1, max_length=264),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='collection',
            name='C_date',
            field=models.CharField(max_length=264),
        ),
    ]
