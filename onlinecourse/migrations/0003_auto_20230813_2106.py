# Generated by Django 3.1.3 on 2023-08-13 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20230813_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
    ]
