# Generated by Django 5.1.3 on 2024-12-12 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_task', '0018_rename_core_name_mfo_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='coreSection',
            new_name='MFOsub',
        ),
    ]
