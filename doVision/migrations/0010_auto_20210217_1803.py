# Generated by Django 3.1.5 on 2021-02-17 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doVision', '0009_auto_20210214_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateTimeField(editable=False),
        ),
    ]