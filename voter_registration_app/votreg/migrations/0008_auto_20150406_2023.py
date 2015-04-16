# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votreg', '0007_auto_20150406_1947'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('url', models.URLField()),
                ('views', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='States',
            new_name='State',
        ),
        migrations.RemoveField(
            model_name='pages',
            name='states',
        ),
        migrations.DeleteModel(
            name='Pages',
        ),
        migrations.AddField(
            model_name='page',
            name='states',
            field=models.ForeignKey(to='votreg.State'),
            preserve_default=True,
        ),
    ]
