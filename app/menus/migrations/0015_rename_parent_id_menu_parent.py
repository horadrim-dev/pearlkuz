# Generated by Django 4.0.4 on 2022-04-23 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0014_rename_parent_menu_parent_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='parent_id',
            new_name='parent',
        ),
    ]
