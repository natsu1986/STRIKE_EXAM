# Generated by Django 4.1.13 on 2024-05-07 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('strikeTaskWeb', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='status',
            new_name='pending_status',
        ),
    ]
