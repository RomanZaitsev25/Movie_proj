# Generated by Django 4.0.3 on 2022-08-01 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0008_alter_movie_choices'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='choices',
            new_name='currency',
        ),
    ]
