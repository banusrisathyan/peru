# Generated by Django 5.0.3 on 2024-04-15 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_tally', '0014_breastfeedingdetail_parentname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='breastfeedingdetail',
            old_name='parentname',
            new_name='parentName',
        ),
    ]
