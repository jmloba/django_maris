# Generated by Django 5.1.3 on 2024-12-19 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_query', '0002_book_store'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='name',
            new_name='bookname',
        ),
    ]
