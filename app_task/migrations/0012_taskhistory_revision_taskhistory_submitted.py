# Generated by Django 5.1.3 on 2024-12-10 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_task', '0011_taskhistory_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskhistory',
            name='revision',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='taskhistory',
            name='submitted',
            field=models.BooleanField(default=False),
        ),
    ]
