# Generated by Django 4.2.11 on 2024-05-24 09:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=50, verbose_name='Место')),
                ('time', models.TimeField(verbose_name='Время')),
                ('action', models.CharField(max_length=300, verbose_name='Действие')),
                ('is_nice', models.BooleanField(default=False, verbose_name='Признак приятной привычки')),
                ('periodicity', models.PositiveIntegerField(choices=[(1, 'Каждый день'), (2, 'Каждую неделю'), (3, 'Каждый будний день'), (4, 'Каждые выходные')], default=1, verbose_name='Периодичность')),
                ('reward', models.CharField(blank=True, max_length=300, null=True, verbose_name='Вознаграждение')),
                ('duration', models.DurationField(verbose_name='Длительность выполнения')),
                ('is_public', models.BooleanField(default=False, verbose_name='Признак публичности')),
                ('related_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='main_habit', to='habits.habit', verbose_name='Связанная привычка')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
                'ordering': ('pk',),
            },
        ),
    ]
