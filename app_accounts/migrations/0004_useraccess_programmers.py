# Generated by Django 5.1.3 on 2024-12-23 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_accounts', '0003_useraccess_post_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccess',
            name='Programmers',
            field=models.BooleanField(default=False),
        ),
    ]
