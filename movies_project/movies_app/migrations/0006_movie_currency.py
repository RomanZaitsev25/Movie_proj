# Generated by Django 4.0.3 on 2022-08-01 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0005_alter_movie_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='currency',
            field=models.CharField(choices=[('E', 'Euro'), ('D', 'Dollars'), ('R', 'Junior')], default='R', max_length=2),
        ),
    ]
