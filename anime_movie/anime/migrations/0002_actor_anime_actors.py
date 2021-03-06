# Generated by Django 4.0.1 on 2022-02-01 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('age', models.PositiveSmallIntegerField(default=0, verbose_name='Возраст')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='actors/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Режиссеры',
                'verbose_name_plural': 'Режиссеры',
            },
        ),
        migrations.AddField(
            model_name='anime',
            name='actors',
            field=models.ManyToManyField(to='anime.Actor', verbose_name='Режиссер'),
        ),
    ]
