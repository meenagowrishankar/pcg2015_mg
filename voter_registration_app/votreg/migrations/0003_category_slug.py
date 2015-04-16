# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('votreg', '0002_auto_20150403_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2015, 4, 4, 4, 14, 36, 841000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
