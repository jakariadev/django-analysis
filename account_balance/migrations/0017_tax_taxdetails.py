# Generated by Django 3.2 on 2021-05-02 06:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account_balance', '0016_auto_20210501_1214'),
    ]

    operations = [
        migrations.CreateModel(
            name='tax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax_country', models.CharField(blank=True, max_length=100, null=True)),
                ('tax_percentage', models.FloatField(blank=True, default=0, null=True)),
                ('country_tax_field', models.CharField(blank=True, default=0, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='taxDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax_amount', models.FloatField(default=0)),
                ('tax_id', models.CharField(max_length=100)),
                ('tax_pay_date', models.DateTimeField(auto_now=True)),
                ('tax_info_law', models.CharField(blank=True, max_length=155, null=True)),
                ('tax_given_area', models.CharField(blank=True, max_length=100, null=True)),
                ('tax_medium', models.CharField(blank=True, max_length=100, null=True)),
                ('tax_description', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
