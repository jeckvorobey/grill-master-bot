# Generated by Django 3.2.9 on 2024-06-10 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_types', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='foodtype',
            options={'verbose_name': 'Тип блюда', 'verbose_name_plural': 'Типы блюд'},
        ),
        migrations.RemoveField(
            model_name='foodtype',
            name='deleted_at',
        ),
        migrations.AlterField(
            model_name='foodtype',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='foodtype',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='foodtype',
            name='label',
            field=models.CharField(max_length=100, verbose_name='Метка'),
        ),
        migrations.AlterField(
            model_name='foodtype',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='foodtype',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Обновлен'),
        ),
    ]