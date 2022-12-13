# Generated by Django 4.1.4 on 2022-12-13 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0005_alter_car_car_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='engine_type',
            field=models.CharField(choices=[('Gasoline', 'Gasoline'), ('Diesel', 'Diesel'), ('Electric', 'Electric'), ('Hybrid', 'Hybrid')], default='Gasoline', max_length=30),
        ),
    ]
