# Generated by Django 4.1.7 on 2023-02-18 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RouletteOwner',
            new_name='RouletteWinner',
        ),
    ]