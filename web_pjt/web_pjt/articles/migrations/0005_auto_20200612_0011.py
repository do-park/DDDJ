# Generated by Django 2.1.15 on 2020-06-11 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20200611_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='movie_title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie'),
        ),
    ]