# Generated by Django 2.2.2 on 2019-06-23 14:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 23, 14, 18, 5, 717851, tzinfo=utc)),
        ),
    ]
