# Generated by Django 3.2 on 2021-06-17 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lipsync', '0009_gptconversation_gptsession'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gptsession',
            name='gpt_character',
        ),
        migrations.RemoveField(
            model_name='gptsession',
            name='user',
        ),
        migrations.DeleteModel(
            name='GptConversation',
        ),
        migrations.DeleteModel(
            name='GptSession',
        ),
    ]
