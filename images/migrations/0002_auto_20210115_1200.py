# Generated by Django 3.1.5 on 2021-01-15 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={},
        ),
        migrations.AddField(
            model_name='image',
            name='rszdimg',
            field=models.ImageField(default=models.ImageField(upload_to='pictures'), upload_to='resized_pictures'),
        ),
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(upload_to='pictures'),
        ),
    ]
