# Generated by Django 4.0.4 on 2022-04-28 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0020_menu_is_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='icon',
            field=models.CharField(default='', help_text='Необязательно. Названия брать отсюда: https://icons.getbootstrap.com/', max_length=30, verbose_name='Иконка'),
        ),
    ]