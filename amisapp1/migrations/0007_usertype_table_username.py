# Generated by Django 2.2.12 on 2020-08-10 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amisapp1', '0006_auto_20200810_0518'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertype_table',
            name='username',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
