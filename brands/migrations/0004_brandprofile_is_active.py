# Generated by Django 3.2.9 on 2022-03-28 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0003_auto_20220302_0734'),
    ]

    operations = [
        migrations.AddField(
            model_name='brandprofile',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
