# Generated by Django 4.1.4 on 2022-12-12 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_listingfavorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
