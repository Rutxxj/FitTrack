# Generated by Django 5.0.1 on 2024-02-04 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FitTrack', '0005_food_remove_foodlog_food_alter_foodlog_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
