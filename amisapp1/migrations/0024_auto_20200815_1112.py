# Generated by Django 2.2.12 on 2020-08-15 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amisapp1', '0023_patientbookappointment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertype_table',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
