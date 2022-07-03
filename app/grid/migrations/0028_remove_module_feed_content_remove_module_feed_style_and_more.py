# Generated by Django 4.0.4 on 2022-06-29 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0039_rename_is_published_menu_published'),
        ('content', '0028_alter_post_image'),
        ('grid', '0027_alter_module_post_html_alter_module_pre_html'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='feed_content',
        ),
        migrations.RemoveField(
            model_name='module',
            name='feed_style',
        ),
        migrations.RemoveField(
            model_name='module',
            name='menu_content',
        ),
        migrations.RemoveField(
            model_name='module',
            name='menu_style',
        ),
        migrations.RemoveField(
            model_name='module',
            name='post_content',
        ),
        migrations.CreateModel(
            name='ModuleContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveSmallIntegerField(blank=True, default=0, help_text='Если оставить равным 0 - добавится в конец.', null=True, verbose_name='Порядок')),
                ('content_type', models.CharField(choices=[('menu', 'Меню'), ('post', 'Пост'), ('feed', 'Лента постов')], default='menu', max_length=64, verbose_name='Тип контента')),
                ('feed_style', models.CharField(choices=[('compact_feed', 'Лента постов (только заголовки)'), ('slider', 'Слайдер постов')], default='compact_feed', max_length=64, verbose_name='Макет ленты постов')),
                ('menu_style', models.CharField(choices=[('horizontal_blocks', 'Горизонтальное меню (блоки)'), ('vertical_with_submenus', 'Вертикальное меню (с дочерними меню)'), ('vertical_without_submenus', 'Вертикальное меню (без дочерних меню)')], default='horizontal_blocks', max_length=64, verbose_name='Макет меню')),
                ('feed_content', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.feed', verbose_name='Лента постов')),
                ('menu_content', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='menu_content', to='menus.menu', verbose_name='Меню')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grid.module', verbose_name='Модуль')),
                ('post_content', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.post', verbose_name='Пост')),
            ],
            options={
                'verbose_name': 'Контент',
                'verbose_name_plural': 'Контент',
                'ordering': ['order'],
            },
        ),
    ]