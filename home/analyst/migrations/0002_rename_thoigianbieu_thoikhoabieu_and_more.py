# Generated by Django 5.2.1 on 2025-06-03 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analyst', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ThoiGianBieu',
            new_name='ThoiKhoaBieu',
        ),
        migrations.RemoveField(
            model_name='hoatdong',
            name='metadata',
        ),
    ]
