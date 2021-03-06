# Generated by Django 3.2 on 2021-04-28 08:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('education', '0009_alter_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='like_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.ManyToManyField(related_name='view_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Teacher', 'Teacher'), ('Student', 'Student')], max_length=100),
        ),
    ]
