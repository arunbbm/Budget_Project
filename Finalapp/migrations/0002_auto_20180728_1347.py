# Generated by Django 2.0.5 on 2018-07-28 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finalapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='E_cheque_date',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='expense',
            name='E_date_of_payment',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='expense',
            name='E_dd_date',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='expense',
            name='E_previous_due_date',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='expense',
            name='E_transaction_date',
            field=models.CharField(max_length=264),
        ),
    ]
