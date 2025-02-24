# Generated by Django 5.1.5 on 2025-01-19 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('email', models.EmailField(max_length=254, verbose_name='EMail')),
                ('adress', models.CharField(max_length=255, verbose_name='Адрес')),
                ('phone', models.BigIntegerField(verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'Контакты',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя отправителя')),
                ('email', models.EmailField(max_length=254, verbose_name='Email отправителя')),
                ('message', models.TextField(verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Оставленный отзыв',
                'verbose_name_plural': 'Оставленный отзыв',
            },
        ),
    ]
