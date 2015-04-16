# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votreg', '0005_remove_category_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choosestate',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='ChooseState',
        ),
    ]
