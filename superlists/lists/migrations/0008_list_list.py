# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0007_auto_20160319_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='list',
            field=models.TextField(default=b''),
        ),
    ]
