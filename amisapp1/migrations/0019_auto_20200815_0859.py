# Generated by Django 2.2.12 on 2020-08-15 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amisapp1', '0018_patientbookappointment_massage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientbookappointment',
            name='date',
            field=models.DateField(default='15.08.2020'),
        ),
    ]
