# Generated by Django 2.2.12 on 2020-08-15 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amisapp1', '0035_dawa_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dawa_category',
            name='user',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
