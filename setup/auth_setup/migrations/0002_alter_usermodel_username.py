# Generated by Django 5.1.1 on 2024-10-08 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_setup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='username',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
