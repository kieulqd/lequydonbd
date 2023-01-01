# Generated by Django 3.2.16 on 2022-12-29 07:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0136_auto_20221221_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problempointsvote',
            name='points',
            field=models.IntegerField(help_text='The amount of points the voter thinks this problem deserves.', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='proposed points'),
        ),
    ]