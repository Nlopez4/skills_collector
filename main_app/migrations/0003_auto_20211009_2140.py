# Generated by Django 3.2.8 on 2021-10-09 21:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_skill'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='gym',
            new_name='gyms',
        ),
        migrations.AddField(
            model_name='skill',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
