# Generated by Django 2.2.12 on 2020-08-16 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amisapp1', '0046_auto_20200816_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientbookappointment',
            name='reject',
            field=models.CharField(default=0, max_length=10, null=True),
        ),
    ]
