# Generated by Django 4.0.3 on 2022-03-24 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoodapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hood',
            name='occupants_Count',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hood',
            name='police_contact',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
