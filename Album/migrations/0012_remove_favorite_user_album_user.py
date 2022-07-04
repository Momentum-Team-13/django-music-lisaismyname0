# Generated by Django 4.0.5 on 2022-07-03 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Album', '0011_user_alter_favorite_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='user',
        ),
        migrations.AddField(
            model_name='album',
            name='user',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='Album.user'),
            preserve_default=False,
        ),
    ]