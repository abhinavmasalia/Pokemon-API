# Generated by Django 3.0 on 2019-12-05 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_app', '0002_auto_20191205_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='serial',
            field=models.IntegerField(null=True),
        ),
    ]
