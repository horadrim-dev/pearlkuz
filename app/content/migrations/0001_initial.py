# Generated by Django 4.0.6 on 2022-08-07 08:50

import ckeditor.fields
import ckeditor_uploader.fields
import content.models
import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=1000, verbose_name='Заголовок')),
                ('alias', models.SlugField(blank=True, default='', help_text="Краткое название транслитом через тире (пример: 'kratkoe-nazvanie-translitom'). Чем короче тем лучше. Для автоматического заполнения - оставьте пустым.", max_length=1000, unique=True)),
                ('published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('published_at', models.DateField(default=datetime.date.today, verbose_name='Дата публикации')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Последнее изменение')),
                ('hits', models.PositiveIntegerField(default=0, verbose_name='Кол-во просмотров')),
                ('feed_style', models.CharField(choices=[('feed', 'Список постов'), ('compact_feed', 'Список постов (только заголовки)'), ('blocks', 'Посты в виде блоков (без изображений)'), ('blocks_with_images_left', 'Посты в виде блоков (изображения слева)'), ('blocks_with_images_top', 'Посты в виде блоков (изображения сверху)'), ('slider', 'Слайдер постов')], default='feed', max_length=64, verbose_name='Макет ленты постов')),
                ('feed_num_columns', models.PositiveSmallIntegerField(choices=[(1, '1 колонка'), (2, '2 колонки'), (3, '3 колонки'), (4, '4 колонки')], default=2, verbose_name='Количество колонок')),
                ('feed_count_items', models.PositiveSmallIntegerField(default=6, verbose_name='Количество выводимых постов')),
                ('feed_readmore', models.BooleanField(default=True, verbose_name='Отображать кнопку "Читать больше"')),
                ('feed_sort_direction', models.CharField(choices=[('horizontal', 'Построчно'), ('vertical', 'По колонкам')], default='horizontal', max_length=16, verbose_name='Направление сортировки')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('menu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='menus.menu', verbose_name='Привязка к меню')),
            ],
            options={
                'verbose_name': 'Лента постов',
                'verbose_name_plural': 'Ленты постов',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=1000, verbose_name='Заголовок')),
                ('alias', models.SlugField(blank=True, default='', help_text="Краткое название транслитом через тире (пример: 'kratkoe-nazvanie-translitom'). Чем короче тем лучше. Для автоматического заполнения - оставьте пустым.", max_length=1000, unique=True)),
                ('published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('published_at', models.DateField(default=datetime.date.today, verbose_name='Дата публикации')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Последнее изменение')),
                ('hits', models.PositiveIntegerField(default=0, verbose_name='Кол-во просмотров')),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/', verbose_name='Изображение поста')),
                ('intro_text', ckeditor.fields.RichTextField(blank=True)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField()),
                ('feed', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.feed', verbose_name='Лента постов')),
                ('menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='menus.menu', verbose_name='Привязка к меню')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ['-published_at'],
            },
        ),
        migrations.CreateModel(
            name='ContentLayout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_style', models.CharField(choices=[('feed', 'Список постов'), ('compact_feed', 'Список постов (только заголовки)'), ('blocks', 'Посты в виде блоков (без изображений)'), ('blocks_with_images_left', 'Посты в виде блоков (изображения слева)'), ('blocks_with_images_top', 'Посты в виде блоков (изображения сверху)'), ('slider', 'Слайдер постов')], default='feed', max_length=64, verbose_name='Макет ленты постов')),
                ('feed_num_columns', models.PositiveSmallIntegerField(choices=[(1, '1 колонка'), (2, '2 колонки'), (3, '3 колонки'), (4, '4 колонки')], default=2, verbose_name='Количество колонок')),
                ('feed_count_items', models.PositiveSmallIntegerField(default=6, verbose_name='Количество выводимых постов')),
                ('feed_readmore', models.BooleanField(default=True, verbose_name='Отображать кнопку "Читать больше"')),
                ('feed_sort_direction', models.CharField(choices=[('horizontal', 'Построчно'), ('vertical', 'По колонкам')], default='horizontal', max_length=16, verbose_name='Направление сортировки')),
                ('menu_style', models.CharField(choices=[('horizontal_blocks', 'Горизонтальное меню (блоки)'), ('vertical_with_submenus', 'Вертикальное меню (с дочерними меню)'), ('vertical_without_submenus', 'Вертикальное меню (без дочерних меню)')], default='horizontal_blocks', max_length=64, verbose_name='Макет меню')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('content_type', models.CharField(choices=[('', '---'), ('post', 'Пост'), ('feed', 'Лента постов'), ('menu', 'Меню')], default='', max_length=64, verbose_name='Тип контента')),
                ('content_feed', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.feed', verbose_name='Лента постов')),
                ('content_menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='menus.menu', verbose_name='Меню')),
                ('content_post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.post', verbose_name='Пост')),
            ],
            options={
                'verbose_name': 'Макет контента',
            },
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=1000, verbose_name='Название')),
                ('extension', models.CharField(blank=True, default='', max_length=16, verbose_name='Расширение файла')),
                ('attached_file', models.FileField(upload_to=content.models.attachment_upload_location, verbose_name='Вложение')),
                ('published_at', models.DateField(default=datetime.date.today, verbose_name='Дата публикации')),
                ('hits', models.PositiveIntegerField(default=0, verbose_name='Кол-во загрузок')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.post', verbose_name='Пост')),
            ],
        ),
        migrations.CreateModel(
            name='ExtraContent',
            fields=[
                ('contentlayout_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='content.contentlayout')),
                ('order', models.PositiveSmallIntegerField(blank=True, default=0, help_text='Если оставить равным 0 - добавится в конец.', null=True, verbose_name='Порядок')),
                ('show_title', models.BooleanField(default=False, verbose_name='Отображать заголовок')),
                ('position', models.CharField(choices=[('right', 'Справа'), ('left', 'Слева'), ('bottom', 'Внизу'), ('top', 'Сверху'), ('stacked', 'Под постом (В виде ленты)')], default='right', max_length=64, verbose_name='Расположение')),
                ('tied_to_menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menus.menu', verbose_name='Привязка к меню')),
            ],
            options={
                'verbose_name': 'дополнительный контент',
                'verbose_name_plural': 'дополнительный контент',
                'ordering': ['order'],
            },
            bases=('content.contentlayout', models.Model),
        ),
    ]
