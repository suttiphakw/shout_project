# Generated by Django 3.2.9 on 2022-03-16 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shouters', '0010_auto_20220221_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='shouter',
            name='ig_reach_source',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='IG => REACH SOURCE (API / PREDICTED)'),
        ),
        migrations.AlterField(
            model_name='shouter',
            name='ig_ad_post_reach',
            field=models.IntegerField(blank=True, null=True, verbose_name='FINAL => EST AD POST REACH'),
        ),
        migrations.AlterField(
            model_name='shouter',
            name='ig_predicted_ad_post_reach',
            field=models.IntegerField(blank=True, null=True, verbose_name='PREDICTED => LOW ADS REACH'),
        ),
    ]
