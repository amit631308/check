# Generated by Django 2.2.12 on 2020-08-15 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amisapp1', '0021_auto_20200815_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientbookappointment',
            name='date',
            field=models.DateField(default='15d.08m.20yyy'),
        ),
    ]