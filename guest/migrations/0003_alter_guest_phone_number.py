# Generated by Django 5.1.7 on 2025-03-13 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0002_alter_guest_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
    ]
