# Generated by Django 2.2.12 on 2020-08-15 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amisapp1', '0024_auto_20200815_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientbookappointment',
            name='profile_pic',
            field=models.ImageField(upload_to=''),
        ),
    ]
