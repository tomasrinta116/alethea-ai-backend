# Generated by Django 3.2 on 2021-06-16 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lipsync', '0003_remove_character_demo_base_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='charactersetting',
            name='gpt',
        ),
    ]
