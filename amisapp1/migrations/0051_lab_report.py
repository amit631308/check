# Generated by Django 2.2.12 on 2020-08-16 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amisapp1', '0050_lab_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='lab_report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100, null=True)),
                ('fname', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('pin', models.CharField(max_length=100, null=True)),
                ('gender', models.CharField(max_length=100, null=True)),
                ('purpose', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
