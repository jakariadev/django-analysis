# Generated by Django 3.2 on 2021-05-01 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_balance', '0014_alter_withdraw_modified_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withdraw',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
