# Generated by Django 4.0.6 on 2022-08-16 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contentlayout',
            name='feed_readmore',
        ),
        migrations.RemoveField(
            model_name='feed',
            name='feed_readmore',
        ),
    ]
