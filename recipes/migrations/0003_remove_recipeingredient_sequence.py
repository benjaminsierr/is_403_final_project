# Generated by Django 3.1.2 on 2020-12-01 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20201201_2010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipeingredient',
            name='sequence',
        ),
    ]
