# Generated by Django 2.2.12 on 2020-08-15 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amisapp1', '0030_auto_20200815_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientbookappointment',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patientbookappointment',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
