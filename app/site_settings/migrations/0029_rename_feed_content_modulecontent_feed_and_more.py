# Generated by Django 4.0.4 on 2022-06-30 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0028_remove_module_feed_content_remove_module_feed_style_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modulecontent',
            old_name='feed_content',
            new_name='feed',
        ),
        migrations.RenameField(
            model_name='modulecontent',
            old_name='menu_content',
            new_name='menu',
        ),
        migrations.RenameField(
            model_name='modulecontent',
            old_name='post_content',
            new_name='post',
        ),
    ]
