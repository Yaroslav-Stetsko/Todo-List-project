# Generated by Django 4.1.3 on 2022-11-14 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='done',
            new_name='task_done',
        ),
    ]
