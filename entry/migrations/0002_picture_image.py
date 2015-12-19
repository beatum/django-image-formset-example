# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='image',
            field=models.ImageField(default=datetime.datetime(2015, 12, 18, 12, 5, 48, 554988, tzinfo=utc), upload_to=b'upload'),
            preserve_default=False,
        ),
    ]
