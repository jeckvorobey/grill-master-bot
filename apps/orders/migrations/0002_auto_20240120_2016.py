# Generated by Django 3.2.9 on 2024-01-20 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='foodorder',
            options={},
        ),
        migrations.RemoveField(
            model_name='foodorder',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='foodorder',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='foodorder',
            name='updated_at',
        ),
    ]
