# Generated by Django 3.2.9 on 2021-11-18 22:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shouter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fb_access_token', models.CharField(blank=True, max_length=500, null=True)),
                ('fb_access_token_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('fb_page_id', models.CharField(blank=True, max_length=120, null=True)),
                ('ig_business_account_id', models.CharField(blank=True, max_length=120, null=True)),
                ('ig_username', models.CharField(blank=True, max_length=120, null=True)),
                ('ig_follower_count', models.IntegerField(blank=True, null=True)),
                ('ig_active_follower', models.IntegerField(blank=True, null=True)),
                ('ig_active_follower_harmonic', models.IntegerField(blank=True, null=True)),
                ('ig_estimated_reach', models.IntegerField(blank=True, null=True)),
                ('ig_total_like', models.IntegerField(blank=True, null=True)),
                ('ig_average_total_like', models.IntegerField(blank=True, null=True)),
                ('ig_like_engagement', models.IntegerField(blank=True, null=True)),
                ('ig_insight', models.JSONField(blank=True, null=True)),
                ('ig_max_total_people', models.IntegerField(blank=True, null=True)),
                ('ig_two_most_common_city', models.JSONField(blank=True, null=True)),
                ('ig_two_most_common_country', models.JSONField(blank=True, null=True)),
                ('ig_two_most_common_gender_age', models.JSONField(blank=True, null=True)),
                ('ig_audience_male_percent', models.FloatField(blank=True, null=True)),
                ('ig_audience_female_percent', models.FloatField(blank=True, null=True)),
                ('ig_age_range_13_17', models.FloatField(blank=True, null=True)),
                ('ig_age_range_18_24', models.FloatField(blank=True, null=True)),
                ('ig_age_range_25_34', models.FloatField(blank=True, null=True)),
                ('ig_age_range_35_44', models.FloatField(blank=True, null=True)),
                ('ig_age_range_45_54', models.FloatField(blank=True, null=True)),
                ('ig_age_range_55_64', models.FloatField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
