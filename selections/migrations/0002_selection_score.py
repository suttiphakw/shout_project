# Generated by Django 3.2.9 on 2022-08-22 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selections', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='selection',
            name='score',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
