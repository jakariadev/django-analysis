# Generated by Django 3.2 on 2021-05-01 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_balance', '0012_auto_20210501_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withdraw',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='withdraw',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
