# Generated by Django 5.0.3 on 2024-05-21 09:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tally', '0054_alter_breastfeedingdetail_submission_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breastfeedingdetail',
            name='submission_date',
            field=models.DateField(default=datetime.date(2024, 5, 21)),
        ),
        migrations.AlterField(
            model_name='poopdetail',
            name='submission_date',
            field=models.DateField(default=datetime.date(2024, 5, 21)),
        ),
        migrations.AlterField(
            model_name='product',
            name='submission_date',
            field=models.DateTimeField(default=datetime.date(2024, 5, 21)),
        ),
    ]
