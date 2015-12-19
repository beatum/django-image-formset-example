# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0004_auto_20151218_1630'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ('-pk',)},
        ),
        migrations.AlterModelOptions(
            name='picture',
            options={'ordering': ('-pk',)},
        ),
    ]
