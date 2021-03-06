# Generated by Django 3.2 on 2021-04-28 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Job",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("mode", models.CharField(blank=True, max_length=271, null=True)),
                ("method", models.CharField(blank=True, max_length=271, null=True)),
                ("audio_key", models.CharField(blank=True, max_length=271, null=True)),
                ("video_key", models.CharField(blank=True, max_length=271, null=True)),
                ("voice_id", models.CharField(blank=True, max_length=271, null=True)),
                (
                    "gtts_language_code",
                    models.CharField(blank=True, max_length=271, null=True),
                ),
                ("gtts_name", models.CharField(blank=True, max_length=271, null=True)),
                ("progress", models.PositiveIntegerField(default=0)),
                ("status", models.CharField(blank=True, max_length=271, null=True)),
                ("result_key", models.CharField(blank=True, max_length=271, null=True)),
                ("job_id", models.CharField(blank=True, max_length=271, null=True)),
                ("inventory_id", models.CharField(max_length=271)),
                ("public_id", models.CharField(max_length=271)),
                ("text", models.CharField(max_length=271)),
                ("animation_task_id", models.CharField(max_length=271)),
                ("image_public_id", models.CharField(max_length=271)),
                ("limit", models.PositiveIntegerField(default=0)),
                ("target_video_key", models.CharField(max_length=271)),
                ("email", models.CharField(max_length=271)),
            ],
        ),
    ]
