# Generated by Django 2.0.4 on 2018-04-19 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('city_guide', '0004_auto_20180419_1654'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attraction_category',
            old_name='id_attracion',
            new_name='id_attraction',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='id_attracion',
            new_name='id_attraction',
        ),
    ]
