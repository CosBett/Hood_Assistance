# Generated by Django 4.0.3 on 2022-03-24 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoodapp', '0002_alter_hood_occupants_count_alter_hood_police_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(upload_to='images/'),
        ),
    ]