# Generated by Django 3.2.9 on 2024-06-10 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0006_auto_20240610_0443'),
        ('users', '0007_auto_20240610_0443'),
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'Корзина', 'verbose_name_plural': 'Корзины'},
        ),
        migrations.AlterModelOptions(
            name='cartfood',
            options={'verbose_name': 'Блюдо в Корзине', 'verbose_name_plural': 'Блюда в Корзине'},
        ),
        migrations.RemoveField(
            model_name='cart',
            name='deleted_at',
        ),
        migrations.AlterField(
            model_name='cart',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='foods',
            field=models.ManyToManyField(through='carts.CartFood', to='foods.Food', verbose_name='Блюда'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Обновлен'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='users.user', verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='cartfood',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carts.cart', verbose_name='Корзина'),
        ),
        migrations.AlterField(
            model_name='cartfood',
            name='food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foods.food', verbose_name='Блюдо'),
        ),
        migrations.AlterField(
            model_name='cartfood',
            name='quantity',
            field=models.PositiveIntegerField(default=1, verbose_name='Количество'),
        ),
    ]
