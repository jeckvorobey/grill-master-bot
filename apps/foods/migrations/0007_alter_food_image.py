# Generated by Django 5.0.6 on 2024-07-20 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0006_auto_20240610_0443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/foods/', verbose_name='Изображение'),
        ),
    ]
