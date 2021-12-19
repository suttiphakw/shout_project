# Generated by Django 3.2.9 on 2021-12-13 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shouters', '0005_shouter_is_already_approve'),
    ]

    operations = [
        migrations.AddField(
            model_name='shouter',
            name='birthday_date',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='shouter',
            name='birthday_month',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='shouter',
            name='birthday_year',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='shouter',
            name='college',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='shouter',
            name='education',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='shouter',
            name='email',
            field=models.EmailField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='shouter',
            name='gender',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='shouter',
            name='is_already_fb_connect',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shouter',
            name='last_name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='shouter',
            name='nickname',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='shouter',
            name='province',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='shouter',
            name='tel',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
