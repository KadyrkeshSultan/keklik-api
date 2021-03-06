# Generated by Django 2.1.1 on 2018-10-15 14:09

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20181005_2152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), help_text='ID правильных вариантов ответов.\nДля Single вопросов массив состоит из одного элемента.\nДля Sequence важен порядок.', size=None)),
                ('answered_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('online', models.BooleanField(db_index=True)),
                ('state', models.CharField(choices=[('players_waiting', 'Ожидание игроков'), ('answering', 'Игроки отвечают на вопросы'), ('check', 'Показ правильного ответа'), ('finish', 'Финиш')], db_index=True, max_length=15)),
                ('timer_on', models.BooleanField(db_index=True, default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('finished_at', models.DateTimeField(db_index=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GeneratedQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variants_order', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), help_text='ID вариантов. При создании новой игры варианты перемешиваются.', size=None)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('finished_at', models.DateTimeField(db_index=True, null=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='question',
            name='number',
            field=models.SmallIntegerField(db_index=True, help_text='Номер вопроса, начиная с 1.\nСоответствует порядковому номеру в массиве.'),
        ),
        migrations.AlterField(
            model_name='question',
            name='timer',
            field=models.DurationField(help_text='Таймер. Null означает, что таймера нет.', null=True),
        ),
        migrations.AddField(
            model_name='generatedquestion',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Question'),
        ),
        migrations.AddField(
            model_name='game',
            name='current_question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='api.GeneratedQuestion'),
        ),
        migrations.AddField(
            model_name='game',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Quiz'),
        ),
        migrations.AddField(
            model_name='game',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Player'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.GeneratedQuestion'),
        ),
    ]
