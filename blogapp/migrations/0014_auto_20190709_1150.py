# Generated by Django 2.2.2 on 2019-07-09 06:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0013_auto_20190709_1132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='owner',
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 9, 6, 20, 29, 37176, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 9, 6, 20, 29, 37176, tzinfo=utc)),
        ),
    ]
