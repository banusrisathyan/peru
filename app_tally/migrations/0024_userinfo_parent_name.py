# Generated by Django 5.0.3 on 2024-04-22 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tally', '0023_remove_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='parent_name',
            field=models.CharField(default='unknown', max_length=100),
        ),
    ]
