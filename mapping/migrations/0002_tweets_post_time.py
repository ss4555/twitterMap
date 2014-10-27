# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweets',
            name='post_time',
            field=models.DateTimeField(default=None),
            preserve_default=False,
        ),
    ]
