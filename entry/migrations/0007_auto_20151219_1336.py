# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0006_remove_picture_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(height_field=400, width_field=400, upload_to=b'upload'),
            preserve_default=True,
        ),
    ]
