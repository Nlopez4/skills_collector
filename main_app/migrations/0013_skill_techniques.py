# Generated by Django 3.2.8 on 2021-10-10 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_remove_skill_class_took'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='techniques',
            field=models.CharField(default=True, max_length=350),
            preserve_default=False,
        ),
    ]
