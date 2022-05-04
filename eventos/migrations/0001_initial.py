# Generated by Django 4.0.4 on 2022-05-04 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('texto', models.TextField()),
                ('localData', models.CharField(max_length=100)),
                ('edicao', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nomes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('evento_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.eventos')),
            ],
        ),
    ]
