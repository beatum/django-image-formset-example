# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0002_picture_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='entry',
            field=models.ForeignKey(blank=True, to='entry.Entry', null=True),
            preserve_default=True,
        ),
    ]
