# Generated by Django 3.2 on 2021-04-24 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0008_auto_20210424_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Student', 'Student'), ('Teacher', 'Teacher')], max_length=100),
        ),
    ]