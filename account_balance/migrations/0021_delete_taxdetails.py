# Generated by Django 3.2 on 2021-05-02 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account_balance', '0020_taxdetails_withdra'),
    ]

    operations = [
        migrations.DeleteModel(
            name='taxDetails',
        ),
    ]
