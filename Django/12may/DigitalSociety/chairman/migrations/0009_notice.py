# Generated by Django 4.2.1 on 2023-06-23 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chairman', '0008_delete_notice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=100)),
                ('media_type', models.CharField(max_length=30)),
                ('pic', models.FileField(blank=True, null=True, upload_to='media/images')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chairman.user')),
            ],
        ),
    ]
