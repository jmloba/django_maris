# Generated by Django 5.1.3 on 2024-12-10 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_task', '0009_tasktable_task_ref'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskhistory',
            name='date_from',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='taskhistory',
            name='date_to',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='taskhistory',
            name='diff',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tasktable',
            name='date_from',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tasktable',
            name='date_to',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
