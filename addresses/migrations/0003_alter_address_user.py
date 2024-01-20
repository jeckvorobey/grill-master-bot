# Generated by Django 3.2.9 on 2024-01-20 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rm_unused_fields'),
        ('addresses', '0002_auto_20240120_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='users.user'),
        ),
    ]
