# Generated by Django 4.0.4 on 2022-04-23 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0010_alter_menu_alias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='alias',
            field=models.SlugField(blank=True, help_text="Краткое название транслитом через тире (пример: 'kratkoe-nazvanie-translitom'. Чем короче тем лучше.", max_length=100),
        ),
    ]
