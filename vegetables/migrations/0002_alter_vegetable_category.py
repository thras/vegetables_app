# Generated by Django 5.1.1 on 2024-10-17 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vegetables', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vegetable',
            name='category',
            field=models.CharField(choices=[('None', '-'), ('Root', 'Root'), ('Stem', 'Stem'), ('Bulb', 'Bulb'), ('Leaf', 'Leaf'), ('Fruit', 'Fruit'), ('Flower', 'Flower'), ('Seed', 'Seed'), ('Tuber', 'Tuber')], default='None', max_length=20),
        ),
    ]