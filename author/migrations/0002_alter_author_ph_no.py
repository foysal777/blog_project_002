# Generated by Django 5.0.6 on 2024-05-30 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='ph_no',
            field=models.IntegerField(max_length=20),
        ),
    ]
