# Generated by Django 4.0.6 on 2022-07-30 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0041_alter_menu_order'),
        ('content', '0042_contentlayout_delete_extracontent'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraContent',
            fields=[
                ('contentlayout_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='content.contentlayout')),
                ('order', models.PositiveSmallIntegerField(blank=True, default=0, help_text='Если оставить равным 0 - добавится в конец.', null=True, verbose_name='Порядок')),
                ('show_title', models.BooleanField(default=False, verbose_name='Отображать заголовок')),
                ('position', models.CharField(choices=[('right', 'Справа'), ('left', 'Слева'), ('bottom', 'Внизу'), ('top', 'Сверху'), ('stacked', 'Под постом (В виде ленты)')], default='right', max_length=64, verbose_name='Расположение')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menus.menu', verbose_name='Привязка к меню')),
            ],
            options={
                'verbose_name': 'Контент',
                'verbose_name_plural': 'Контент',
                'ordering': ['order'],
            },
            bases=('content.contentlayout', models.Model),
        ),
    ]