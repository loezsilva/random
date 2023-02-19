# Generated by Django 4.1.7 on 2023-02-17 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roulette',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome da rifa')),
                ('max_numbers', models.SmallIntegerField(default=50, verbose_name='Quantidade máxima de números')),
                ('file', models.FileField(blank=True, max_length=4000, null=True, upload_to='', verbose_name='Imagem da rifa')),
                ('spins', models.SmallIntegerField(blank=True, default=0, verbose_name='Quantidade de giros')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Registrado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
        ),
        migrations.CreateModel(
            name='RouletteOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Registrado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client', verbose_name='Vencedor')),
                ('roulette', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.roulette', verbose_name='Rifa')),
            ],
        ),
        migrations.CreateModel(
            name='RouletteNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50, verbose_name='Número do bilhete')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Registrado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client', verbose_name='Cliente')),
                ('roulette', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.roulette', verbose_name='Rifa')),
            ],
        ),
    ]