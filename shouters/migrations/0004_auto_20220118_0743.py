# Generated by Django 3.2.9 on 2022-01-18 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shouters', '0003_auto_20220117_0820'),
    ]

    operations = [
        migrations.AddField(
            model_name='shouter',
            name='book_bank_photo',
            field=models.ImageField(blank=True, upload_to='book_bank/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='shouter',
            name='id_card_photo',
            field=models.ImageField(blank=True, upload_to='id_card/%Y/%m/%d/'),
        ),
    ]
