# Generated by Django 4.0.4 on 2022-06-06 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grid', '0003_remove_block_order_alter_section_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='order',
            field=models.PositiveSmallIntegerField(blank=True, default=0, help_text='Если оставить равным 0 - добавится в конец.', null=True, verbose_name='Порядок'),
        ),
    ]