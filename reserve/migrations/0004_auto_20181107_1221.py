# Generated by Django 2.1.1 on 2018-11-07 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0003_auto_20181106_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserve',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]