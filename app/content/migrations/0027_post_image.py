# Generated by Django 4.0.4 on 2022-06-21 04:12

import content.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0026_alter_feed_options_alter_post_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=content.models.attachment_upload_location, verbose_name='Изображение поста'),
        ),
    ]
