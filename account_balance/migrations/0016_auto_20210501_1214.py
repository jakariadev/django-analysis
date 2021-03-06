# Generated by Django 3.2 on 2021-05-01 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_balance', '0015_alter_withdraw_modified_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdraw',
            name='cashout_pur_tot',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='withdraw',
            name='current_pur_tot',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='withdraw',
            name='prev_pur_tot',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
