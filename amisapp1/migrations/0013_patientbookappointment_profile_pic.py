# Generated by Django 2.2.12 on 2020-08-15 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amisapp1', '0012_usertype_table_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientbookappointment',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
