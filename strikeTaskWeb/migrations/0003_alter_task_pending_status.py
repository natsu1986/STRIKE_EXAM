# Generated by Django 4.1.13 on 2024-05-07 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strikeTaskWeb', '0002_rename_status_task_pending_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='pending_status',
            field=models.BooleanField(default=True),
        ),
    ]
