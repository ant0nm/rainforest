# Generated by Django 2.1.7 on 2019-03-08 19:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rainforest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=500, validators=[django.core.validators.MinLengthValidator(limit_value=10)]),
        ),
    ]
