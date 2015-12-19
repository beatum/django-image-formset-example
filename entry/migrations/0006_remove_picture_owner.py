# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0005_auto_20151219_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='owner',
        ),
    ]
