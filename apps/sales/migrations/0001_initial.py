# Generated by Django 3.2.9 on 2024-01-20 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=255)),
                ('value', models.IntegerField(help_text='Скидка в процентах')),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]