# Generated by Django 5.1.3 on 2024-12-10 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_task', '0007_taskhistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskhistory',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
