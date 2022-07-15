# Generated by Django 4.0.5 on 2022-07-13 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grid', '0032_alter_module_options_modulecontent_feed_num_columns_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='modulecontent',
            name='feed_count_posts',
            field=models.PositiveSmallIntegerField(default=6, verbose_name='Количество выводимых постов'),
        ),
        migrations.AlterField(
            model_name='modulecontent',
            name='feed_num_columns',
            field=models.PositiveSmallIntegerField(choices=[(1, '1 колонка'), (2, '2 колонки'), (3, '3 колонки'), (4, '4 колонки')], default=2, verbose_name='Количество колонок'),
        ),
    ]
