# Generated by Django 4.2.2 on 2023-07-01 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imsapp', '0009_alter_clubs_club_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(default='01/07/2023'),
        ),
    ]
