# Generated by Django 3.2 on 2021-05-20 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_widgetuseraccess'),
    ]

    operations = [
        migrations.AddField(
            model_name='widgetuseraccess',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
