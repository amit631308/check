# Generated by Django 2.2.12 on 2020-08-16 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amisapp1', '0048_auto_20200816_1205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientbookappointment',
            old_name='reject',
            new_name='status',
        ),
        migrations.RemoveField(
            model_name='patientbookappointment',
            name='accept',
        ),
    ]
