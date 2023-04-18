# Generated by Django 4.1.7 on 2023-04-18 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_movie_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=255)),
                ('text', models.TextField(blank=True, null=True)),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='director',
            name='slug',
            field=models.SlugField(default='no-slug'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='avg_rating',
            field=models.FloatField(default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.SlugField(default='no-slug'),
            preserve_default=False,
        ),
    ]