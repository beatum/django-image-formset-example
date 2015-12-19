# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0008_auto_20151219_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to=b'upload'),
            preserve_default=True,
        ),
    ]
