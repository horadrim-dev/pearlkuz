# Generated by Django 4.0.6 on 2022-08-22 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_post_image_position_alter_feed_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(default='', max_length=256, verbose_name='Теги'),
        ),
    ]
