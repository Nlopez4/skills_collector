# Generated by Django 3.2.8 on 2021-10-10 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_skill_class_took'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='class_took',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
