# Generated by Django 3.2.9 on 2022-08-30 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ig_active_follower_percent',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
