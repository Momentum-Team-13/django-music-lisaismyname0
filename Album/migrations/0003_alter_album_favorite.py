# Generated by Django 4.0.5 on 2022-07-05 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Album', '0002_album_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='favorite',
            field=models.BooleanField(default='False'),
        ),
    ]