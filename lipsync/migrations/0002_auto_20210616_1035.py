# Generated by Django 3.2 on 2021-06-16 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lipsync', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleTTS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('language_code', models.CharField(default='en-US', max_length=50)),
                ('language_name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='character',
            name='language_code',
        ),
        migrations.RemoveField(
            model_name='character',
            name='language_name',
        ),
        migrations.AddField(
            model_name='character',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='charactersetting',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='uploadrecording',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='character',
            name='language',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='language', to='lipsync.googletts'),
            preserve_default=False,
        ),
    ]
