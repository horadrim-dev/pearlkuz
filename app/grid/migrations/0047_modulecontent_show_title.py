# Generated by Django 4.0.5 on 2022-07-24 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grid', '0046_delete_widget'),
    ]

    operations = [
        migrations.AddField(
            model_name='modulecontent',
            name='show_title',
            field=models.BooleanField(default=True, verbose_name='Отображать заголовок'),
        ),
    ]
