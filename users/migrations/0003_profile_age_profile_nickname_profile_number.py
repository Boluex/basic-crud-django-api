# Generated by Django 4.1 on 2022-09-11 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AddField(
            model_name='profile',
            name='nickname',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AddField(
            model_name='profile',
            name='number',
            field=models.CharField(blank=True, max_length=2000),
        ),
    ]
