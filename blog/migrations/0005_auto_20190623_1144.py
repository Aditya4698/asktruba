# Generated by Django 2.2.2 on 2019-06-23 18:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190623_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 23, 18, 44, 9, 864176, tzinfo=utc)),
        ),
    ]
